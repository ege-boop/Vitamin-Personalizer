from lab_data import LabData
from user import User
from lab_result import LabResult
from lab_analyzer import LabAnalyzer
from datetime import datetime
import random
import string

class LabInfo:
    def __init__(self):
        self.data = LabData()
        self.analyzer = LabAnalyzer()
    
    def generate_user_id(self):
        while True:
            user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
            if not self.data.user_exists(user_id):
                return user_id
    
    def add_user(self, name, age, sex, height, weight):
        try:
            if age < 1 or age > 120:
                return False, "Age must be between 1 and 120."
            
            if height < 50 or height > 300:
                return False, "Height must be between 50 and 300 cm."
            
            if weight < 20 or weight > 500:
                return False, "Weight must be between 20 and 500 kg."
            
            if sex.lower() not in ['male', 'female']:
                return False, "Sex must be 'male' or 'female'."
            
            user_id = self.generate_user_id()
            user = User(user_id, name, age, sex, height, weight)
            self.data.add_user(user)
            return True, f"User added successfully with ID: {user_id}"
        
        except Exception as e:
            return False, f"Error adding user: {str(e)}"
    
    def login_user(self, user_id):
        try:
            user = self.data.get_user(user_id.upper())
            if user:
                return True, user
            else:
                return False, "User not found."
        except Exception as e:
            return False, f"Error during login: {str(e)}"
    
    def add_lab_results(self, user_id, lab_values):
        try:
            lab_result = LabResult(
                user_id=user_id,
                wbc=lab_values.get('wbc'),
                rbc=lab_values.get('rbc'),
                hemoglobin=lab_values.get('hemoglobin'),
                hematocrit=lab_values.get('hematocrit'),
                platelet_count=lab_values.get('platelet_count'),
                mcv=lab_values.get('mcv'),
                mch=lab_values.get('mch'),
                mchc=lab_values.get('mchc'),
                rdw=lab_values.get('rdw'),
                mpv=lab_values.get('mpv'),
                neutrophils=lab_values.get('neutrophils'),
                lymphocytes=lab_values.get('lymphocytes'),
                monocytes=lab_values.get('monocytes'),
                eosinophils=lab_values.get('eosinophils'),
                basophils=lab_values.get('basophils'),
                glucose=lab_values.get('glucose'),
                sodium=lab_values.get('sodium'),
                potassium=lab_values.get('potassium'),
                chloride=lab_values.get('chloride'),
                co2=lab_values.get('co2'),
                bun=lab_values.get('bun'),
                creatinine=lab_values.get('creatinine'),
                total_protein=lab_values.get('total_protein'),
                albumin=lab_values.get('albumin'),
                total_bilirubin=lab_values.get('total_bilirubin'),
                alkaline_phosphatase=lab_values.get('alkaline_phosphatase'),
                alt=lab_values.get('alt'),
                ast=lab_values.get('ast'),
                calcium=lab_values.get('calcium'),
                total_cholesterol=lab_values.get('total_cholesterol'),
                triglycerides=lab_values.get('triglycerides'),
                hdl_cholesterol=lab_values.get('hdl_cholesterol'),
                ldl_cholesterol=lab_values.get('ldl_cholesterol'),
                tsh=lab_values.get('tsh'),
                free_t4=lab_values.get('free_t4'),
                free_t3=lab_values.get('free_t3'),
                vitamin_d=lab_values.get('vitamin_d'),
                vitamin_b12=lab_values.get('vitamin_b12'),
                folate=lab_values.get('folate'),
                iron=lab_values.get('iron'),
                ferritin=lab_values.get('ferritin'),
                tibc=lab_values.get('tibc'),
                hemoglobin_a1c=lab_values.get('hemoglobin_a1c'),
                insulin=lab_values.get('insulin'),
                uric_acid=lab_values.get('uric_acid'),
                crp=lab_values.get('crp'),
                esr=lab_values.get('esr'),
                psa=lab_values.get('psa'),
                magnesium=lab_values.get('magnesium'),
                phosphorus=lab_values.get('phosphorus'),
                timestamp=datetime.now().isoformat()
            )
            
            self.data.add_lab_results(lab_result)
            return True, "Lab results added successfully."
        
        except Exception as e:
            return False, f"Error adding lab results: {str(e)}"
    
    def update_lab_results(self, user_id, lab_values):
        try:
            lab_result = LabResult(
                user_id=user_id,
                wbc=lab_values.get('wbc'),
                rbc=lab_values.get('rbc'),
                hemoglobin=lab_values.get('hemoglobin'),
                hematocrit=lab_values.get('hematocrit'),
                platelet_count=lab_values.get('platelet_count'),
                mcv=lab_values.get('mcv'),
                mch=lab_values.get('mch'),
                mchc=lab_values.get('mchc'),
                rdw=lab_values.get('rdw'),
                mpv=lab_values.get('mpv'),
                neutrophils=lab_values.get('neutrophils'),
                lymphocytes=lab_values.get('lymphocytes'),
                monocytes=lab_values.get('monocytes'),
                eosinophils=lab_values.get('eosinophils'),
                basophils=lab_values.get('basophils'),
                glucose=lab_values.get('glucose'),
                sodium=lab_values.get('sodium'),
                potassium=lab_values.get('potassium'),
                chloride=lab_values.get('chloride'),
                co2=lab_values.get('co2'),
                bun=lab_values.get('bun'),
                creatinine=lab_values.get('creatinine'),
                total_protein=lab_values.get('total_protein'),
                albumin=lab_values.get('albumin'),
                total_bilirubin=lab_values.get('total_bilirubin'),
                alkaline_phosphatase=lab_values.get('alkaline_phosphatase'),
                alt=lab_values.get('alt'),
                ast=lab_values.get('ast'),
                calcium=lab_values.get('calcium'),
                total_cholesterol=lab_values.get('total_cholesterol'),
                triglycerides=lab_values.get('triglycerides'),
                hdl_cholesterol=lab_values.get('hdl_cholesterol'),
                ldl_cholesterol=lab_values.get('ldl_cholesterol'),
                tsh=lab_values.get('tsh'),
                free_t4=lab_values.get('free_t4'),
                free_t3=lab_values.get('free_t3'),
                vitamin_d=lab_values.get('vitamin_d'),
                vitamin_b12=lab_values.get('vitamin_b12'),
                folate=lab_values.get('folate'),
                iron=lab_values.get('iron'),
                ferritin=lab_values.get('ferritin'),
                tibc=lab_values.get('tibc'),
                hemoglobin_a1c=lab_values.get('hemoglobin_a1c'),
                insulin=lab_values.get('insulin'),
                uric_acid=lab_values.get('uric_acid'),
                crp=lab_values.get('crp'),
                esr=lab_values.get('esr'),
                psa=lab_values.get('psa'),
                magnesium=lab_values.get('magnesium'),
                phosphorus=lab_values.get('phosphorus'),
                timestamp=datetime.now().isoformat()
            )
            
            self.data.update_lab_results(lab_result)
            return True, "Lab results updated successfully."
        
        except Exception as e:
            return False, f"Error updating lab results: {str(e)}"
    
    def get_analysis(self, user_id):
        try:
            user = self.data.get_user(user_id)
            lab_results = self.data.get_latest_lab_results(user_id)
            
            if not user or not lab_results:
                return None, "User or lab results not found."
            
            analysis = {}
            lab_tests = [
                ('wbc', 'White Blood Cells'),
                ('rbc', 'Red Blood Cells'),
                ('hemoglobin', 'Hemoglobin'),
                ('hematocrit', 'Hematocrit'),
                ('platelet_count', 'Platelet Count'),
                ('mcv', 'Mean Corpuscular Volume'),
                ('mch', 'Mean Corpuscular Hemoglobin'),
                ('mchc', 'Mean Corpuscular Hemoglobin Concentration'),
                ('rdw', 'Red Cell Distribution Width'),
                ('mpv', 'Mean Platelet Volume'),
                ('neutrophils', 'Neutrophils'),
                ('lymphocytes', 'Lymphocytes'),
                ('monocytes', 'Monocytes'),
                ('eosinophils', 'Eosinophils'),
                ('basophils', 'Basophils'),
                ('glucose', 'Glucose'),
                ('sodium', 'Sodium'),
                ('potassium', 'Potassium'),
                ('chloride', 'Chloride'),
                ('co2', 'Carbon Dioxide'),
                ('bun', 'Blood Urea Nitrogen'),
                ('creatinine', 'Creatinine'),
                ('total_protein', 'Total Protein'),
                ('albumin', 'Albumin'),
                ('total_bilirubin', 'Total Bilirubin'),
                ('alkaline_phosphatase', 'Alkaline Phosphatase'),
                ('alt', 'ALT'),
                ('ast', 'AST'),
                ('calcium', 'Calcium'),
                ('total_cholesterol', 'Total Cholesterol'),
                ('triglycerides', 'Triglycerides'),
                ('hdl_cholesterol', 'HDL Cholesterol'),
                ('ldl_cholesterol', 'LDL Cholesterol'),
                ('tsh', 'TSH'),
                ('free_t4', 'Free T4'),
                ('free_t3', 'Free T3'),
                ('vitamin_d', 'Vitamin D'),
                ('vitamin_b12', 'Vitamin B12'),
                ('folate', 'Folate'),
                ('iron', 'Iron'),
                ('ferritin', 'Ferritin'),
                ('tibc', 'TIBC'),
                ('hemoglobin_a1c', 'Hemoglobin A1C'),
                ('insulin', 'Insulin'),
                ('uric_acid', 'Uric Acid'),
                ('crp', 'C-Reactive Protein'),
                ('esr', 'ESR'),
                ('psa', 'PSA'),
                ('magnesium', 'Magnesium'),
                ('phosphorus', 'Phosphorus')
            ]
            
            for test_key, test_name in lab_tests:
                value = getattr(lab_results, test_key)
                if value is not None:
                    classification = self.analyzer.classify_value(test_key, value, user.sex)
                    recommendations = self.analyzer.get_recommendations(test_key, classification)
                    unit = self.analyzer.reference_ranges[test_key]['unit']
                    source = self.analyzer.reference_ranges[test_key]['source']
                    
                    analysis[test_name] = {
                        'value': value,
                        'unit': unit,
                        'status': classification,
                        'recommendations': recommendations,
                        'source': source
                    }
            
            return analysis, None
        
        except Exception as e:
            return None, f"Error generating analysis: {str(e)}"