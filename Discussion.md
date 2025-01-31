### **How I Reached This Solution**  

Given the problem of efficiently extracting logs from a **1 TB** log file, I needed a solution that:  
**Processes large files efficiently** without loading everything into memory.  
**Filters logs based on a specific date** while keeping the format intact.  
**Handles errors gracefully** to avoid crashes or unexpected failures.  

#### **Step-by-Step Approach:**  

**Basic Filtering Logic:**  
   - First, I started with a simple loop that **reads the file line by line** and checks if each line starts with the target date.  
   - If it matches, it gets written to an output file.  

**Optimizing for Large Files:**  
   - Since loading a **1 TB file into memory is impractical**, I used **line-by-line streaming** (`with open(...)`) to ensure efficient reading.  

**Handling File and Directory Issues:**  
   - Used `os.makedirs(output_dir, exist_ok=True)` to **ensure the output directory exist** before writing the logs.  
   - Wrapped file operations in a `try-except` block to catch `FileNotFoundError` and other unexpected issue.  

**Making the Script More User-Friendly:**  
   - Added **command-line arguments** so users can specify the date dynamically.  
   - Provided **clear error messages** instead of cryptic Python traceback.  

#### **Final Result:**  
A clean, efficient script that **extracts logs for a given date from a massive log file without using excessive memory**.  


