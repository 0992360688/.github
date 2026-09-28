from typing import List

class Role:
    def __init__(self, name: str, permissions: List[str]):
        self.name = name
        self.permissions = permissions

# Define some example roles
ADMIN_ROLE = Role("admin", ["create_user", "delete_user", "view_user"])
USER_ROLE = Role("user", ["view_user"])

# Role-based access control logic
roles = {
    "admin": ADMIN_ROLE,
    "user": USER_ROLE,
}

def has_permission(role_name: str, permission: str) -> bool:
    """Check if a role has a specific permission."""
    role = roles.get(role_name)
    if role:
        return permission in role.permissions
    return False

def get_user_role(user) -> str:
    """Map the user's superuser flag to the corresponding role."""
    return "admin" if getattr(user, "is_superuser", False) else "user"

def authorize(role_name: str, permission: str) -> bool:
    """Authorize a user based on their role and required permission."""
    return has_permission(role_name, permission)