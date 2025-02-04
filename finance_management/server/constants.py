class CategoryType:
    INCOME = "income"
    EXPENSE = "expense"

    CHOICES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense")
    ]


class CategoryGroup:
    # Expense
    LIVING_EXPENSE = "living_expense"
    INCIDENTAL_EXPENSE = "incidental_expense"
    FIXED_EXPENSE = "fixed_expense"
    INVESTMENT_SAVING = "investment_saving"

    EXPENSE_CHOICES = [
        (INCIDENTAL_EXPENSE, "Incidental Expense"),
        (FIXED_EXPENSE, "Fixed Expense"),
        (INVESTMENT_SAVING, "Investment Saving")
    ]
