import time
from abc import ABC, abstractmethod

# Interface for the data service, defining the contract for both Real Subject and Proxy
class IDataService(ABC):
    @abstractmethod
    def get_data(self, user_role: str) -> str:
        pass

# Real Subject: The actual service that fetches sensitive data
class RealDataService(IDataService):
    def get_data(self, user_role: str) -> str:
        print(f"RealDataService: Fetching sensitive data for role '{user_role}'...")
        time.sleep(2)  # Simulate a time-consuming operation like a database query or API call
        return f"Sensitive data for {user_role}"

# Proxy: Controls access and provides caching for the RealDataService
class DataServiceProxy(IDataService):
    def __init__(self, real_service: RealDataService, allowed_roles: list):
        self._real_service = real_service
        self._cache = {}
        self._allowed_roles = allowed_roles
        print(f"DataServiceProxy: Initialized with allowed roles: {', '.join(allowed_roles)}")

    def get_data(self, user_role: str) -> str:
        # Proxy: Access Control - Check if the user role is allowed to perform this operation
        if user_role not in self._allowed_roles:
            print(f"DataServiceProxy: Access DENIED for role '{user_role}'. Not in allowed roles.")
            raise PermissionError(f"Role '{user_role}' is not authorized to access this data.")

        # Proxy: Caching - Check if data is already in cache for this user_role
        if user_role in self._cache:
            print(f"DataServiceProxy: Returning cached data for role '{user_role}'.")
            return self._cache[user_role]

        # If not in cache and access is allowed, delegate the request to the real service
        print(f"DataServiceProxy: Data not in cache for role '{user_role}'. Fetching from real service...")
        data = self._real_service.get_data(user_role)
        self._cache[user_role] = data  # Cache the fetched data for future requests
        print(f"DataServiceProxy: Data for role '{user_role}' cached.")
        return data

# Client code that interacts with the service via the proxy
if __name__ == "__main__":
    real_service = RealDataService()
    # Create a proxy that allows 'admin' and 'user' roles to access data
    proxy = DataServiceProxy(real_service, allowed_roles=["admin", "user"])

    print("\n--- Attempting access with 'admin' role (first time) ---")
    # First call for 'admin' will hit the real service and cache the result
    admin_data_1 = proxy.get_data("admin")
    print(f"Client received: {admin_data_1}")

    print("\n--- Attempting access with 'admin' role (second time - should be cached) ---")
    # Second call for 'admin' will return cached data immediately, skipping the real service delay
    admin_data_2 = proxy.get_data("admin")
    print(f"Client received: {admin_data_2}")

    print("\n--- Attempting access with 'user' role (first time) ---")
    # First call for 'user' will hit the real service and cache the result
    user_data_1 = proxy.get_data("user")
    print(f"Client received: {user_data_1}")

    print("\n--- Attempting access with 'guest' role (should be denied by proxy) ---")
    try:
        # 'guest' role is not in allowed_roles, so the proxy denies access
        guest_data = proxy.get_data("guest")
        print(f"Client received: {guest_data}")
    except PermissionError as e:
        print(f"Client caught error: {e}")

    print("\n--- Attempting access with 'admin' role again (still cached) ---")
    # Subsequent calls for 'admin' will continue to return cached data
    admin_data_3 = proxy.get_data("admin")
    print(f"Client received: {admin_data_3}")
