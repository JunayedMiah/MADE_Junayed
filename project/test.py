import os
import subprocess
import unittest

class TestPipeline(unittest.TestCase):
    
    # Define output file paths
    OUTPUT_DIR = "data"
    DB1 = os.path.join(OUTPUT_DIR, "crash_reporting.db")
    DB2 = os.path.join(OUTPUT_DIR, "vehicle_collision.db")

    @classmethod
    def setUpClass(cls):
        """This method will run once before all test cases"""
        # Ensure the output directory is clean before the test
        if os.path.exists(cls.DB1):
            os.remove(cls.DB1)
        if os.path.exists(cls.DB2):
            os.remove(cls.DB2)

    def test_pipeline_runs(self):
        """Test if the pipeline runs and generates output files"""
        # Run the pipeline (this will execute the pipeline.py script)
        result = subprocess.run(['python3', 'project/pipeline.py'], capture_output=True, text=True)

        # Assert that the pipeline ran without errors
        self.assertEqual(result.returncode, 0, f"Pipeline failed with error: {result.stderr}")

    def test_output_files_created(self):
        """Test if the output files (databases) are created"""
        # Run the pipeline first
        subprocess.run(['python3', 'project/pipeline.py'], check=True)

        # Check if the output files exist
        self.assertTrue(os.path.exists(self.DB1), "The crash_reporting.db file was not created.")
        self.assertTrue(os.path.exists(self.DB2), "The vehicle_collision.db file was not created.")
    
    @classmethod
    def tearDownClass(cls):
        """This method will run once after all test cases"""
        # Clean up the output files after tests
        if os.path.exists(cls.DB1):
            os.remove(cls.DB1)
        if os.path.exists(cls.DB2):
            os.remove(cls.DB2)

if __name__ == "__main__":
    unittest.main()
