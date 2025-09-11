from lab_info import LabInfo
from summary import MedicalReportGenerator
from vitamin_dictionary import VitaminDictionary
from datetime import datetime
import os

def save_user_id(user_id, user_name):
    try:
        # userid saver 
        userid_dir = "userid"
        if not os.path.exists(userid_dir):
            os.makedirs(userid_dir)
            print(f"Created directory: {userid_dir}")
        
        filename = f"User_ID_{user_name.replace(' ', '_')}_{user_id}.txt"
        filepath = os.path.join(userid_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(f"VITAMIN PERSONALIZER - USER CREDENTIALS\n")
            f.write(f"=" * 50 + "\n")
            f.write(f"User Name: {user_name}\n")
            f.write(f"User ID: {user_id}\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"=" * 50 + "\n")
            f.write(f"IMPORTANT: Save this ID to login again!\n")
            f.write(f"Keep this file safe - you need this ID to access your account.\n")
        
        print(f"\n User ID saved to file: {filepath}")
        print(f"File location: {os.path.abspath(filepath)}")
        return True
    except Exception as e:
        print(f" Could not save ID file: {e}")
        return False

def display_menu():
    print("\n" + "="*50)
    print("       Welcome to Vitamin Personalizer!")
    print("="*50)
    print("1. New User")
    print("2. Login")
    print("3. Update Data")
    print("4. Generate PDF Report")
    print("5. Vitamin Dictionary")
    print("6. Exit")
    print("="*50)
    return input("Enter your choice (1-6): ")

def get_lab_values():
    lab_tests = [
        ('wbc', 'White Blood Cells (×10³/µL)'),
        ('rbc', 'Red Blood Cells (×10⁶/µL)'),
        ('hemoglobin', 'Hemoglobin (g/dL)'),
        ('hematocrit', 'Hematocrit (%)'),
        ('platelet_count', 'Platelet Count (×10³/µL)'),
        ('mcv', 'Mean Corpuscular Volume (fL)'),
        ('mch', 'Mean Corpuscular Hemoglobin (pg)'),
        ('mchc', 'Mean Corpuscular Hemoglobin Concentration (g/dL)'),
        ('rdw', 'Red Cell Distribution Width (%)'),
        ('mpv', 'Mean Platelet Volume (fL)'),
        ('neutrophils', 'Neutrophils (%)'),
        ('lymphocytes', 'Lymphocytes (%)'),
        ('monocytes', 'Monocytes (%)'),
        ('eosinophils', 'Eosinophils (%)'),
        ('basophils', 'Basophils (%)'),
        ('glucose', 'Glucose (mg/dL)'),
        ('sodium', 'Sodium (mmol/L)'),
        ('potassium', 'Potassium (mmol/L)'),
        ('chloride', 'Chloride (mmol/L)'),
        ('co2', 'Carbon Dioxide (mmol/L)'),
        ('bun', 'Blood Urea Nitrogen (mg/dL)'),
        ('creatinine', 'Creatinine (mg/dL)'),
        ('total_protein', 'Total Protein (g/dL)'),
        ('albumin', 'Albumin (g/dL)'),
        ('total_bilirubin', 'Total Bilirubin (mg/dL)'),
        ('alkaline_phosphatase', 'Alkaline Phosphatase (U/L)'),
        ('alt', 'ALT (U/L)'),
        ('ast', 'AST (U/L)'),
        ('calcium', 'Calcium (mg/dL)'),
        ('total_cholesterol', 'Total Cholesterol (mg/dL)'),
        ('triglycerides', 'Triglycerides (mg/dL)'),
        ('hdl_cholesterol', 'HDL Cholesterol (mg/dL)'),
        ('ldl_cholesterol', 'LDL Cholesterol (mg/dL)'),
        ('tsh', 'TSH (mIU/L)'),
        ('free_t4', 'Free T4 (ng/dL)'),
        ('free_t3', 'Free T3 (pg/mL)'),
        ('vitamin_d', 'Vitamin D (ng/mL)'),
        ('vitamin_b12', 'Vitamin B12 (pg/mL)'),
        ('folate', 'Folate (ng/mL)'),
        ('iron', 'Iron (µg/dL)'),
        ('ferritin', 'Ferritin (ng/mL)'),
        ('tibc', 'TIBC (µg/dL)'),
        ('hemoglobin_a1c', 'Hemoglobin A1C (%)'),
        ('insulin', 'Insulin (µIU/mL)'),
        ('uric_acid', 'Uric Acid (mg/dL)'),
        ('crp', 'C-Reactive Protein (mg/L)'),
        ('esr', 'ESR (mm/hr)'),
        ('psa', 'PSA (ng/mL)'),
        ('magnesium', 'Magnesium (mg/dL)'),
        ('phosphorus', 'Phosphorus (mg/dL)')
    ]
    
    lab_values = {}
    print("\nEnter your lab test values (press Enter or type N/A to skip any test):")
    print("-" * 70)
    
    for test_key, test_name in lab_tests:
        while True:
            try:
                value_input = input(f"{test_name}: ").strip()
                if value_input == "" or value_input.lower() in ['n/a', 'na']:
                    lab_values[test_key] = None
                    break
                else:
                    value = float(value_input)
                    if value < 0:
                        print("Value cannot be negative. Please try again.")
                        continue
                    lab_values[test_key] = value
                    break
            except ValueError:
                print("Please enter a valid number, press Enter, or type N/A to skip.")
    
    return lab_values

def display_analysis(analysis, user_name):
    print(f"\n{'='*80}")
    print(f"                    ANALYSIS RESULTS FOR {user_name.upper()}")
    print(f"{'='*80}")
    
    normal_results = []
    abnormal_results = []
    
    for test_name, result in analysis.items():
        if result['status'] == 'Normal':
            normal_results.append((test_name, result))
        else:
            abnormal_results.append((test_name, result))
    
    if abnormal_results:
        print(f"\nRESULTS REQUIRING ATTENTION:")
        print("-" * 80)
        for test_name, result in abnormal_results:
            status_symbol = "LOW" if result['status'] == 'Low' else "HIGH"
            print(f"[{status_symbol}] {test_name}: {result['value']} {result['unit']} - {result['status']}")
            print(f"         Source: {result['source']}")
            
            if result['recommendations']:
                print(f"         Supplement: {result['recommendations']['supplement']}")
                print(f"         Diet: {result['recommendations']['diet']}")
            print()
    
    if normal_results:
        print(f"\nNORMAL RESULTS:")
        print("-" * 80)
        for test_name, result in normal_results:
            print(f"[NORMAL] {test_name}: {result['value']} {result['unit']} - {result['status']}")
    
    print(f"\n{'='*80}")
    print("NOTE: Consult with your healthcare provider before making")
    print("      significant changes to your diet or supplement routine.")
    print(f"{'='*80}")

def main():
    info = LabInfo()
    report_generator = MedicalReportGenerator()
    vitamin_dict = VitaminDictionary()
    current_user = None
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            print("\nNEW USER REGISTRATION")
            print("-" * 30)
            
            while True:
                name = input("Enter Full Name: ").strip()
                if name and name.replace(" ", "").replace("-", "").replace("'", "").isalpha():
                    break
                else:
                    print("Name must contain only letters, spaces, hyphens, or apostrophes.")
            
            while True:
                try:
                    age = int(input("Enter Age: "))
                    if 1 <= age <= 120:
                        break
                    else:
                        print("Age must be between 1 and 120.")
                except ValueError:
                    print("Please enter a valid age.")
            
            while True:
                sex = input("Enter Sex (Male/Female): ").strip().lower()
                if sex in ['male', 'female']:
                    break
                else:
                    print("Please enter 'Male' or 'Female'.")
            
            while True:
                try:
                    height = float(input("Enter Height (cm): "))
                    if 50 <= height <= 300:
                        break
                    else:
                        print("Height must be between 50 and 300 cm.")
                except ValueError:
                    print("Please enter a valid height.")
            
            while True:
                try:
                    weight = float(input("Enter Weight (kg): "))
                    if 20 <= weight <= 500:
                        break
                    else:
                        print("Weight must be between 20 and 500 kg.")
                except ValueError:
                    print("Please enter a valid weight.")
            
            success, message = info.add_user(name, age, sex, height, weight)
            print(f"\n{message}")
            
            if success:
                user_id = message.split(": ")[1]
                
                # Save user ID to file
                save_user_id(user_id, name)
                
                proceed = input("\nWould you like to enter lab test values now? (y/n): ").lower()
                if proceed == 'y':
                    lab_values = get_lab_values()
                    success, message = info.add_lab_results(user_id, lab_values)
                    print(f"\n{message}")
                    
                    if success:
                        current_user = user_id
                        analysis, error = info.get_analysis(user_id)
                        if analysis:
                            display_analysis(analysis, name)
                        else:
                            print(f"Error generating analysis: {error}")
        
        elif choice == '2':
            print("\nUSER LOGIN")
            print("-" * 20)
            user_id = input("Enter User ID: ").strip().upper()
            
            success, result = info.login_user(user_id)
            if success:
                current_user = user_id
                print(f"\nWelcome back, {result.name}!")
                print(f"User Details: {result}")
                
                analysis, error = info.get_analysis(user_id)
                if analysis:
                    display_analysis(analysis, result.name)
                else:
                    print("\nNo lab results found. Use option 3 to add lab data.")
            else:
                print(f"\nERROR: {result}")
        
        elif choice == '3':
            if current_user is None:
                print("\nPlease login first (option 2).")
                continue
            
            print(f"\nUPDATE LAB DATA FOR USER: {current_user}")
            print("-" * 50)
            
            lab_values = get_lab_values()
            success, message = info.update_lab_results(current_user, lab_values)
            print(f"\n{message}")
            
            if success:
                _, user = info.login_user(current_user)
                analysis, error = info.get_analysis(current_user)
                if analysis:
                    display_analysis(analysis, user.name)
                else:
                    print(f"Error generating analysis: {error}")
        
        elif choice == '4':
            if current_user is None:
                print("\nPlease login first (option 2).")
                continue
            
            print(f"\nGENERATE PDF REPORT FOR USER: {current_user}")
            print("-" * 50)
            
            _, user = info.login_user(current_user)
            analysis, error = info.get_analysis(current_user)
            
            if analysis:
                success, message = report_generator.generate_pdf_report(user, analysis)
                print(f"\n{message}")
            else:
                print(f"Error: {error}")
        
        elif choice == '5':
            vitamin_dict.show_all_vitamins()
            input("\nPress Enter to continue...")
        
        elif choice == '6':
            print("\nThank you for using Vitamin Personalizer!")
            print("Stay healthy!")
            break
        
        else:
            print("\nInvalid choice. Please select a valid option (1-6).")

if __name__ == "__main__":
    main()