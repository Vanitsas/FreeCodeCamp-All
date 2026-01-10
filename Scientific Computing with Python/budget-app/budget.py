def create_spend_chart(categories):
    spent = []
    for c in categories:
        spent.append(
            sum(-item["amount"] for item in c.ledger if item["amount"] < 0)
        )

    total = sum(spent)
    percentages = [(s / total) * 100 for s in spent]
    rounded = [int(p // 10) * 10 for p in percentages]

    lines = ["Percentage spent by category"]

    for i in range(100, -1, -10):
        line = f"{str(i).rjust(3)}| "
        for p in rounded:
            line += "o  " if p >= i else "   "
        lines.append(line)

    lines.append("    " + "-" * (len(categories) * 3 + 1))

    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        line = "     "
        for c in categories:
            line += (c.name[i] if i < len(c.name) else " ") + "  "
        lines.append(line)

    return "\n".join(lines)
