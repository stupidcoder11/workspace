'''
### POINTS TO REMEMBER

1. Singleton ensures a class has only one instance and provides a global point of access to it.
2. In Python, singletons are often implemented using a class-level instance and a factory/getter method, module-level singletons, or metaclasses.

When to Use Singleton Pattern (IDENTIFY CAREFULLY) -
✅ You need a single shared resource (e.g., logger, configuration, connection pool)
✅ You want a single point of access to state that should be globally consistent

Advantages -
✅ Controlled access to the single instance
✅ Useful for shared resources where multiple instances would cause problems

Disadvantages and Caveats -
❌ Can introduce global state and hidden dependencies, making testing and reasoning harder
❌ Breaks single-responsibility / can become a god object if misused
❌ Not thread-safe by default — concurrent access during initialization can create multiple instances

Testing notes -
- Prefer passing dependencies explicitly (dependency injection) in testable code rather than relying on singletons.
- If you use a singleton, add clear reset/teardown hooks for tests.

Implementation notes - this file shows a simple, non-thread-safe example. For production use,
consider a thread-safe initialization (locks) or using module-level singletons which are simpler in Python.
'''


class Logger:
    _instance = None

    def __init__(self):
        # Initialize any required state here
        pass
    
    @staticmethod
    def get_instance():
        # Simple lazy initialization (NOT thread-safe)
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def info(self, message: str):
        print(f"INFO: {message}")
    
    def warning(self, message: str):
        print(f"WARNING: {message}")
    
    def error(self, message: str):
        print(f"ERROR: {message}")
    

if __name__ == "__main__":
    # demo usage
    l1 = Logger.get_instance()
    l2 = Logger.get_instance()
    assert l1 is l2
    l1.info("This is a log message.")
    l2.warning("This is another log message.")