def get_fields(user=None):
    return {
        "id": user.id,
        "u": user.username,
        "fn": user.first_name,
        "ln": user.last_name,
        "e": user.email,
    }
