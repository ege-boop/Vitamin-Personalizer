class LabAnalyzer:
    def __init__(self):
        self.reference_ranges = {
            'wbc': {'low': 4.0, 'high': 11.0, 'unit': '×10³/µL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9109'},
            'rbc': {'low': {'male': 4.5, 'female': 4.0}, 'high': {'male': 5.9, 'female': 5.2}, 'unit': '×10⁶/µL', 'source': 'https://testdirectory.questdiagnostics.com/test/test-detail/518/complete-blood-count-cbc-with-differential'},
            'hemoglobin': {'low': {'male': 13.5, 'female': 12.0}, 'high': {'male': 17.5, 'female': 15.5}, 'unit': 'g/dL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9106'},
            'hematocrit': {'low': {'male': 41, 'female': 36}, 'high': {'male': 50, 'female': 44}, 'unit': '%', 'source': 'https://www.labcorp.com/tests/005009/complete-blood-count-cbc-with-differential'},
            'platelet_count': {'low': 150, 'high': 450, 'unit': '×10³/µL', 'source': 'https://testdirectory.questdiagnostics.com/test/test-detail/518/complete-blood-count-cbc-with-differential'},
            'mcv': {'low': 80, 'high': 100, 'unit': 'fL', 'source': 'https://www.labcorp.com/tests/005009/complete-blood-count-cbc-with-differential'},
            'mch': {'low': 27, 'high': 33, 'unit': 'pg', 'source': 'https://www.labcorp.com/tests/005009/complete-blood-count-cbc-with-differential'},
            'mchc': {'low': 32, 'high': 36, 'unit': 'g/dL', 'source': 'https://www.labcorp.com/tests/005009/complete-blood-count-cbc-with-differential'},
            'rdw': {'low': 11.5, 'high': 14.5, 'unit': '%', 'source': 'https://testdirectory.questdiagnostics.com/test/test-detail/518/complete-blood-count-cbc-with-differential'},
            'mpv': {'low': 7.4, 'high': 10.4, 'unit': 'fL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9109'},
            'neutrophils': {'low': 45, 'high': 70, 'unit': '%', 'source': 'https://www.labcorp.com/tests/005009/complete-blood-count-cbc-with-differential'},
            'lymphocytes': {'low': 20, 'high': 45, 'unit': '%', 'source': 'https://www.labcorp.com/tests/005009/complete-blood-count-cbc-with-differential'},
            'monocytes': {'low': 2, 'high': 10, 'unit': '%', 'source': 'https://www.labcorp.com/tests/005009/complete-blood-count-cbc-with-differential'},
            'eosinophils': {'low': 1, 'high': 4, 'unit': '%', 'source': 'https://www.labcorp.com/tests/005009/complete-blood-count-cbc-with-differential'},
            'basophils': {'low': 0, 'high': 2, 'unit': '%', 'source': 'https://www.labcorp.com/tests/005009/complete-blood-count-cbc-with-differential'},
            'glucose': {'low': 70, 'high': 99, 'unit': 'mg/dL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8472'},
            'sodium': {'low': 136, 'high': 145, 'unit': 'mmol/L', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9290'},
            'potassium': {'low': 3.5, 'high': 5.1, 'unit': 'mmol/L', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8359'},
            'chloride': {'low': 98, 'high': 107, 'unit': 'mmol/L', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9067'},
            'co2': {'low': 22, 'high': 29, 'unit': 'mmol/L', 'source': 'https://testdirectory.questdiagnostics.com/test/test-detail/399/carbon-dioxide-total'},
            'bun': {'low': 6, 'high': 24, 'unit': 'mg/dL', 'source': 'https://www.labcorp.com/tests/001008/urea-nitrogen-bun'},
            'creatinine': {'low': {'male': 0.7, 'female': 0.6}, 'high': {'male': 1.3, 'female': 1.1}, 'unit': 'mg/dL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8500'},
            'total_protein': {'low': 6.0, 'high': 8.3, 'unit': 'g/dL', 'source': 'https://testdirectory.questdiagnostics.com/test/test-detail/395/protein-total'},
            'albumin': {'low': 3.5, 'high': 5.0, 'unit': 'g/dL', 'source': 'https://www.labcorp.com/tests/001230/albumin'},
            'total_bilirubin': {'low': 0.2, 'high': 1.2, 'unit': 'mg/dL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8452'},
            'alkaline_phosphatase': {'low': 44, 'high': 147, 'unit': 'U/L', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8362'},
            'alt': {'high': 56, 'unit': 'U/L', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8391'},
            'ast': {'high': 40, 'unit': 'U/L', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8430'},
            'calcium': {'low': 8.5, 'high': 10.5, 'unit': 'mg/dL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8093'},
            'total_cholesterol': {'high': 200, 'unit': 'mg/dL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9048'},
            'triglycerides': {'high': 150, 'unit': 'mg/dL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9200'},
            'hdl_cholesterol': {'low': {'male': 40, 'female': 50}, 'unit': 'mg/dL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9048'},
            'ldl_cholesterol': {'high': 100, 'unit': 'mg/dL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9048'},
            'tsh': {'low': 0.4, 'high': 4.0, 'unit': 'mIU/L', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8544'},
            'free_t4': {'low': 0.8, 'high': 1.8, 'unit': 'ng/dL', 'source': 'https://testdirectory.questdiagnostics.com/test/test-detail/587/t4-free'},
            'free_t3': {'low': 2.3, 'high': 4.2, 'unit': 'pg/mL', 'source': 'https://www.labcorp.com/tests/004259/triiodothyronine-t3-free'},
            'vitamin_d': {'low': 30, 'high': 100, 'unit': 'ng/mL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8421'},
            'vitamin_b12': {'low': 200, 'high': 900, 'unit': 'pg/mL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9289'},
            'folate': {'low': 2.7, 'high': 17.0, 'unit': 'ng/mL', 'source': 'https://testdirectory.questdiagnostics.com/test/test-detail/733/folate-serum'},
            'iron': {'low': {'male': 65, 'female': 50}, 'high': {'male': 175, 'female': 170}, 'unit': 'µg/dL', 'source': 'https://www.labcorp.com/tests/001321/iron-and-total-iron-binding-capacity-tibc'},
            'ferritin': {'low': {'male': 30, 'female': 15}, 'high': {'male': 400, 'female': 150}, 'unit': 'ng/mL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/9437'},
            'tibc': {'low': 250, 'high': 450, 'unit': 'µg/dL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8344'},
            'hemoglobin_a1c': {'low': 4.0, 'high': 5.6, 'unit': '%', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8633'},
            'insulin': {'low': 2.6, 'high': 24.9, 'unit': 'µIU/mL', 'source': 'https://testdirectory.questdiagnostics.com/test/test-detail/480/insulin'},
            'uric_acid': {'low': {'male': 3.4, 'female': 2.4}, 'high': {'male': 7.0, 'female': 6.0}, 'unit': 'mg/dL', 'source': 'https://www.labcorp.com/tests/001057/uric-acid'},
            'crp': {'high': 3.0, 'unit': 'mg/L', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8498'},
            'esr': {'high': {'male': 15, 'female': 20}, 'unit': 'mm/hr', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8407'},
            'psa': {'high': 4.0, 'unit': 'ng/mL', 'source': 'https://www.mayocliniclabs.com/test-catalog/overview/8863'},
            'magnesium': {'low': 1.7, 'high': 2.2, 'unit': 'mg/dL', 'source': 'https://www.labcorp.com/tests/001081/magnesium'},
            'phosphorus': {'low': 2.5, 'high': 4.5, 'unit': 'mg/dL', 'source': 'https://testdirectory.questdiagnostics.com/test/test-detail/798/phosphorus'}
        }
        
        self.recommendations = {
            'wbc': {
                'low': {'supplement': 'Zinc and Vitamin C supplements', 'diet': 'Immune-boosting foods, good hygiene'},
                'high': {'supplement': 'Consult doctor immediately', 'diet': 'Anti-inflammatory diet, consult doctor'}
            },
            'rbc': {
                'low': {'supplement': 'Iron and B12 supplements', 'diet': 'Iron-rich foods, B12 sources'},
                'high': {'supplement': 'Increase hydration', 'diet': 'Hydration, monitor altitude exposure'}
            },
            'hemoglobin': {
                'low': {'supplement': 'Iron supplement', 'diet': 'Spinach, red meat, iron-rich foods'},
                'high': {'supplement': 'Increase hydration', 'diet': 'Hydrate well, avoid smoking'}
            },
            'hematocrit': {
                'low': {'supplement': 'Iron supplement', 'diet': 'Iron-rich foods, proper hydration'},
                'high': {'supplement': 'Increase fluid intake', 'diet': 'Drink more water, monitor'}
            },
            'platelet_count': {
                'low': {'supplement': 'B12 and folate supplements', 'diet': 'B12 and folate rich foods'},
                'high': {'supplement': 'Increase hydration', 'diet': 'Hydrate well, anti-inflammatory diet'}
            },
            'glucose': {
                'low': {'supplement': 'None needed', 'diet': 'Small frequent meals, complex carbs'},
                'high': {'supplement': 'Consult doctor', 'diet': 'Low-carb diet, avoid sugars and refined carbs'}
            },
            'total_cholesterol': {
                'high': {'supplement': 'Fish oil, plant sterols', 'diet': 'Oats, fiber, avoid fried foods'}
            },
            'triglycerides': {
                'high': {'supplement': 'Omega-3 supplements', 'diet': 'Low-sugar, low-alcohol, more fiber'}
            },
            'hdl_cholesterol': {
                'low': {'supplement': 'Omega-3 supplements', 'diet': 'Olive oil, avocado, exercise regularly'}
            },
            'ldl_cholesterol': {
                'high': {'supplement': 'Plant sterols, fiber supplements', 'diet': 'Avoid saturated fat, eat nuts, oatmeal'}
            },
            'tsh': {
                'low': {'supplement': 'Consult endocrinologist', 'diet': 'Avoid excessive iodine'},
                'high': {'supplement': 'Selenium supplement', 'diet': 'Iodine-rich foods, consult endocrinologist'}
            },
            'vitamin_d': {
                'low': {'supplement': 'Take 2000-4000 IU/day', 'diet': 'Fatty fish, egg yolks, fortified milk'},
                'high': {'supplement': 'Stop vitamin D supplements', 'diet': 'Hydrate well, maintain normal diet'}
            },
            'vitamin_b12': {
                'low': {'supplement': 'B12 supplements (1000-2000 mcg)', 'diet': 'Fish, eggs, dairy, fortified cereals'},
                'high': {'supplement': 'Stop B12 supplements', 'diet': 'Maintain normal diet'}
            },
            'folate': {
                'low': {'supplement': 'Folic acid supplement', 'diet': 'Leafy greens, citrus fruits, fortified grains'},
                'high': {'supplement': 'Continue current intake', 'diet': 'Maintain current diet'}
            },
            'iron': {
                'low': {'supplement': 'Ferrous sulfate supplement', 'diet': 'Red meat, spinach, legumes, vitamin C foods'},
                'high': {'supplement': 'Avoid iron supplements', 'diet': 'Avoid red meat, check ferritin, consult doctor'}
            },
            'ferritin': {
                'low': {'supplement': 'Iron supplement', 'diet': 'Beans, lean meats, fortified cereals'},
                'high': {'supplement': 'Avoid iron supplements', 'diet': 'Anti-inflammatory foods, check liver function'}
            },
            'alt': {
                'high': {'supplement': 'Milk thistle supplement', 'diet': 'Avoid alcohol, fried food, support liver health'}
            },
            'ast': {
                'high': {'supplement': 'Milk thistle supplement', 'diet': 'Avoid alcohol, support liver health'}
            }
        }
    
    def classify_value(self, test_name, value, sex):
        if value is None:
            return "Not tested"
        
        ranges = self.reference_ranges[test_name]
        
        if isinstance(ranges.get('low'), dict):
            low_threshold = ranges['low'][sex.lower()]
        else:
            low_threshold = ranges.get('low')
        
        if isinstance(ranges.get('high'), dict):
            high_threshold = ranges['high'][sex.lower()]
        else:
            high_threshold = ranges.get('high')
        
        if test_name in ['total_cholesterol', 'triglycerides', 'ldl_cholesterol', 'alt', 'ast', 'crp', 'esr', 'psa']:
            if value > high_threshold:
                return "High"
            else:
                return "Normal"
        
        if test_name == 'hdl_cholesterol':
            if value < low_threshold:
                return "Low"
            else:
                return "Normal"
        
        if low_threshold and value < low_threshold:
            return "Low"
        elif high_threshold and value > high_threshold:
            return "High"
        else:
            return "Normal"
    
    def get_recommendations(self, test_name, classification):
        if test_name in self.recommendations and classification.lower() in self.recommendations[test_name]:
            return self.recommendations[test_name][classification.lower()]
        return None