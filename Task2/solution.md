### **Solution: Performance Testing Exercise**

#### **1. Optimal Pair of Test Cases**  
The pair **TC5 (Deposit → Transfer with Discount) + TC2 (Check Balance → Change PIN)** covers the **most functionalities** (5 out of 6).

#### **2. Covered Functionalities**  
- **F1**: Apply discount (via TC5).  
- **F2**: Check balance (via TC2).  
- **F3**: Change PIN (via TC2).  
- **F5**: Transfer funds (via TC5).  
- **F6**: Deposit checks (via TC5).  

#### **3. Uncovered Functionality**  
- **F4**: View/print transaction statements (only covered in TC4 and TC6).  

---

### **Step-by-Step Explanation**  
1. **Map Test Cases to Functionalities**:  
   - TC1: F1, F2  
   - TC2: F2, F3  
   - TC3: F3  
   - TC4: F4, F5  
   - TC5: F1, F5, F6  
   - TC6: F4, F6  

2. **Evaluate Combinations**:  
   - **TC5 + TC2**: Covers **F1, F2, F3, F5, F6** (5 functionalities).  
   - Other pairs (e.g., TC5 + TC4) cover only 4 functionalities.  

3. **Uncovered Functionality**:  
   - **F4** (view/print statements) is only tested in TC4 or TC6.  

---

### **Key Takeaway**  
By prioritizing **TC5 and TC2**, you test **83% of functionalities** (5/6) while missing only F4. This maximizes coverage under time constraints.