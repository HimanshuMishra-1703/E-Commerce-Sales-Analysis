import pandas as pd
from ollama import chat


# =========================================================
# 1. LOAD DATA
# =========================================================

orders = pd.read_csv("data/raw/List of Orders.csv")
details = pd.read_csv("data/raw/Order Details.csv")
targets = pd.read_csv("data/raw/Sales target.csv")

# =========================================================
# 2. PREPARE DATA
# =========================================================

# Merge order information with order details
df = pd.merge(
    details,
    orders,
    on="Order ID",
    how="left"
)

# Convert Order Date into datetime
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True,
    errors="coerce"
)

# Create Month column
df["Month"] = df["Order Date"].dt.strftime("%B")

# Create Year-Month column
df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)


# =========================================================
# 3. ANALYTICAL TOOLS
# =========================================================


def get_profit_by_category() -> str:
    """
    Use this function when the user asks about profit
    by category, highest profit category, lowest profit
    category, or most profitable category.
    """

    result = (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_string()


def get_sales_by_category() -> str:
    """
    Use this function when the user asks about sales
    by category, highest sales category, lowest sales
    category, or best selling category.
    """

    result = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_string()


def get_profit_by_state() -> str:
    """
    Use this function when the user asks about profit
    by state, highest profit state, lowest profit state,
    or most profitable state.
    """

    result = (
        df.groupby("State")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_string()


def get_sales_by_state() -> str:
    """
    Use this function when the user asks about sales
    by state, highest sales state, lowest sales state,
    or best performing state by sales.
    """

    result = (
        df.groupby("State")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_string()


def get_monthly_sales() -> str:
    """
    Use this function when the user asks about monthly sales,
    sales by month, monthly sales trend, or best sales month.
    """

    result = (
        df.groupby("Month")["Amount"]
        .sum()
    )

    # Put months in calendar order
    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    result = result.reindex(month_order).dropna()

    return result.to_string()


def get_monthly_profit() -> str:
    """
    Use this function when the user asks about monthly profit,
    profit by month, profit trend, or best profit month.
    """

    result = (
        df.groupby("Month")["Profit"]
        .sum()
    )

    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    result = result.reindex(month_order).dropna()

    return result.to_string()


def get_loss_making_categories() -> str:
    """
    Use this function when the user asks about loss-making
    categories, categories with negative profit, or categories
    generating losses.
    """

    result = (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values()
    )

    loss_making = result[result < 0]

    if loss_making.empty:
        return "No category has an overall negative profit."

    return loss_making.to_string()


def get_loss_making_subcategories() -> str:
    """
    Use this function when the user asks about loss-making
    sub-categories, sub-categories with negative profit,
    or products groups generating losses.
    """

    result = (
        df.groupby("Sub-Category")["Profit"]
        .sum()
        .sort_values()
    )

    loss_making = result[result < 0]

    if loss_making.empty:
        return "No sub-category has an overall negative profit."

    return loss_making.to_string()


def get_sales_vs_target() -> str:
    """
    Use this function when the user asks about sales targets,
    actual sales versus target, target achievement, or whether
    sales exceeded the target.
    """

    actual = (
        df.groupby(["Month", "Category"])["Amount"]
        .sum()
        .reset_index()
    )

    target = targets.copy()

    # Rename target column if required
    target = target.rename(
        columns={
            "Month of Order Date": "Month"
        }
    )

    merged = pd.merge(
        actual,
        target,
        on=["Month", "Category"],
        how="left"
    )

    merged["Variance"] = (
        merged["Amount"] - merged["Target"]
    )

    merged["Achievement %"] = (
        merged["Amount"] / merged["Target"] * 100
    )

    result = merged[
        [
            "Month",
            "Category",
            "Amount",
            "Target",
            "Variance",
            "Achievement %"
        ]
    ]

    return result.to_string(index=False)


def get_overall_summary() -> str:
    """
    Use this function when the user asks for an overall
    e-commerce business summary or overall performance.
    """

    total_sales = df["Amount"].sum()
    total_profit = df["Profit"].sum()
    total_quantity = df["Quantity"].sum()
    total_orders = df["Order ID"].nunique()

    return f"""
Total Sales: {total_sales:.2f}
Total Profit: {total_profit:.2f}
Total Quantity Sold: {total_quantity}
Total Orders: {total_orders}
"""


def get_total_sales() -> str:
    """
    Use this function when the user asks for total sales,
    revenue, or overall sales amount.
    """

    return f"Total Sales: {df['Amount'].sum():.2f}"


def get_total_profit() -> str:
    """
    Use this function when the user asks for total profit
    or overall profit.
    """

    return f"Total Profit: {df['Profit'].sum():.2f}"


def get_total_quantity() -> str:
    """
    Use this function when the user asks for total quantity
    sold or total units.
    """

    return f"Total Quantity Sold: {df['Quantity'].sum()}"


def get_total_orders() -> str:
    """
    Use this function when the user asks for total orders
    or number of orders.
    """

    return f"Total Orders: {df['Order ID'].nunique()}"


def get_average_order_value() -> str:
    """
    Use this function when the user asks about average order
    value, average sales per order, or AOV.
    """

    total_sales = df["Amount"].sum()
    total_orders = df["Order ID"].nunique()

    if total_orders == 0:
        return "Average Order Value cannot be calculated."

    aov = total_sales / total_orders

    return f"Average Order Value: {aov:.2f}"


def get_category_performance() -> str:
    """
    Use this function when the user asks to compare categories
    using both sales and profit.
    """

    result = (
        df.groupby("Category")
        .agg(
            Sales=("Amount", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
        .sort_values("Sales", ascending=False)
    )

    return result.to_string()


def get_subcategory_performance() -> str:
    """
    Use this function when the user asks to compare
    sub-categories using sales and profit.
    """

    result = (
        df.groupby("Sub-Category")
        .agg(
            Sales=("Amount", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
        .sort_values("Sales", ascending=False)
    )

    return result.to_string()

def get_sales_vs_profit_by_category() -> str:
    """
    Compare sales and profit for each category.
    Use this when the user asks about categories with
    high sales but low profit.
    """

    result = (
        df.groupby("Category")
        .agg(
            Sales=("Amount", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values("Sales", ascending=False)
    )

    return result.to_string()


# =========================================================
# 4. MAKE TOOLS AVAILABLE TO AI
# =========================================================

available_functions = {

    "get_profit_by_category":
        get_profit_by_category,

    "get_sales_by_category":
        get_sales_by_category,

    "get_profit_by_state":
        get_profit_by_state,

    "get_sales_by_state":
        get_sales_by_state,

    "get_monthly_sales":
        get_monthly_sales,

    "get_monthly_profit":
        get_monthly_profit,

    "get_loss_making_categories":
        get_loss_making_categories,

    "get_loss_making_subcategories":
        get_loss_making_subcategories,

    "get_sales_vs_target":
        get_sales_vs_target,

    "get_overall_summary":
        get_overall_summary,

    "get_total_sales":
        get_total_sales,

    "get_total_profit":
        get_total_profit,

    "get_total_quantity":
        get_total_quantity,

    "get_total_orders":
        get_total_orders,

    "get_average_order_value":
        get_average_order_value,

    "get_category_performance":
        get_category_performance,

    "get_subcategory_performance":
        get_subcategory_performance
}


tools = list(available_functions.values())


# =========================================================
# 5. AI INSTRUCTIONS
# =========================================================

system_message = """
You are an AI business analyst for an e-commerce sales analytics project.

Your job is to answer business questions using the analytical
Python tools provided to you.

IMPORTANT RULES:

1. Use the appropriate analytical tool when the question requires
   information from the dataset.

2. Never invent sales, profit, quantity, state, category, or target
   values.

3. Do not calculate important business numbers yourself if a tool
   can provide the validated result.

4. After receiving the tool result, explain it in simple business
   language.

5. Do not infer profitability, popularity, customer preference,
   or any other business metric unless the tool result actually
   contains evidence for it.

6. Only make conclusions that are supported by the calculated data..

7. If the user asks something that the available tools cannot answer,
   clearly say that the current analytics system does not support
   that question.

8. Keep answers concise but provide useful business interpretation.

9. Distinguish between sales and profit.
"""


# =========================================================
# 6. ASK QUESTIONS CONTINUOUSLY
# =========================================================

print("\n==============================================")
print("   AI E-COMMERCE BUSINESS ANALYST")
print("==============================================")

print("\nYou can ask questions such as:")
print("- Which category has the highest sales?")
print("- Which category has the highest profit?")
print("- Which state has the highest sales?")
print("- Which state has the highest profit?")
print("- Show me monthly sales.")
print("- Which categories are loss making?")
print("- Compare sales and profit by category.")
print("- How are sales performing against target?")
print("- Give me an overall business summary.")
print("- What is the average order value?")
print("\nType 'exit' to stop.\n")


while True:

    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("\nAI Analyst closed.")
        break


    messages = [
        {
            "role": "system",
            "content": system_message
        },
        {
            "role": "user",
            "content": user_question
        }
    ]


    # =====================================================
    # 7. AI + TOOL-CALLING LOOP
    # =====================================================

    while True:

        response = chat(
            model="llama3.2:3b",
            messages=messages,
            tools=tools
        )

        # Add AI response to conversation
        messages.append(response.message)


        # Check whether AI wants to call a tool
        if response.message.tool_calls:

            for tool_call in response.message.tool_calls:

                function_name = tool_call.function.name

                print(
                    f"\nAI called: {function_name}"
                )


                # Find the correct Python function
                function_to_call = available_functions.get(
                    function_name
                )


                if function_to_call:

                    # Execute Python/Pandas analysis
                    result = function_to_call()
                  

                    print("\nPython calculated:")
                    print(result)


                    # Send result back to AI
                    messages.append(
                        {
                            "role": "tool",
                            "content": str(result),
                            "tool_name": function_name
                        }
                    )

                else:

                    messages.append(
                        {
                            "role": "tool",
                            "content": "Tool not found.",
                            "tool_name": function_name
                        }
                    )


        else:

            # No more tools required
            break


    # =====================================================
    # 8. DISPLAY FINAL AI ANSWER
    # =====================================================

    print("\n===== AI BUSINESS INSIGHT =====\n")

    print(response.message.content)

    print("\n----------------------------------------------\n")