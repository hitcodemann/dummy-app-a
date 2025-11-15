# Simulate importing from dummy-app-b and dummy-app-c
# In real Jenkins, it will clone them as git submodules or install via pip
# For demo, we're just showing the dependency structure

def run_pipeline(num_steps=5, force_fail=False):
    """
    Main pipeline: Depends on math_utils and logger.
    If they fail → whole pipeline fails.
    """
    try:
        # Simulate importing math_utils
        from math_utils import calculate_build_time
        # Simulate importing logger
        from logger import log_build_status
    except ImportError as e:
        print(f"Dependency missing! {e}")
        print("Pipeline FAILED: Missing dependency")
        return

    try:
        if force_fail:
            build_time = calculate_build_time(0)  # This will trigger failure
        else:
            build_time = calculate_build_time(num_steps)
        
        log_build_status('success', f'Build completed in {build_time}s')
        print("Pipeline SUCCESS: All dependencies worked!")
        
    except ValueError as e:
        log_build_status('fail', str(e))
        print(f"Pipeline FAILURE: {e}")
        raise

# Test runs
if __name__ == "__main__":
    print("=== NORMAL RUN ===")
    run_pipeline(0)  # Success
    
    print("\n=== FAILURE SIMULATION ===")
    run_pipeline(5, force_fail=True)  # This will fail
