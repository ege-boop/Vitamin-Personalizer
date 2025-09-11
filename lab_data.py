import sqlite3
from datetime import datetime
from user import User
from lab_result import LabResult

class LabData:
    def __init__(self, db_name="medical_lab.db"):
        self.db_name = db_name
        self.create_tables()
    
    def get_connection(self):
        """Create a new connection for each database operation"""
        return sqlite3.connect(self.db_name)
    
    def reset_database(self):
        """Delete and recreate tables if there are column issues"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS lab_results')
        cursor.execute('DROP TABLE IF EXISTS users')
        conn.commit()
        conn.close()
        self.create_tables()
        print("Database reset successfully!")
    
    def create_tables(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            sex TEXT NOT NULL,
            height REAL NOT NULL,
            weight REAL NOT NULL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS lab_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            -- Complete Blood Count (CBC)
            wbc REAL, 
            rbc REAL, 
            hemoglobin REAL, 
            hematocrit REAL, 
            platelet_count REAL,
            mcv REAL, 
            mch REAL, 
            mchc REAL, 
            rdw REAL, 
            mpv REAL,
            -- CBC Differential
            neutrophils REAL, 
            lymphocytes REAL, 
            monocytes REAL, 
            eosinophils REAL, 
            basophils REAL,
            -- Basic Metabolic Panel
            glucose REAL, 
            sodium REAL, 
            potassium REAL, 
            chloride REAL, 
            co2 REAL,
            bun REAL, 
            creatinine REAL,
            -- Liver Function
            total_protein REAL, 
            albumin REAL, 
            total_bilirubin REAL,
            alkaline_phosphatase REAL, 
            alt REAL, 
            ast REAL,
            -- Minerals
            calcium REAL,
            magnesium REAL, 
            phosphorus REAL,
            -- Lipid Panel
            total_cholesterol REAL, 
            triglycerides REAL, 
            hdl_cholesterol REAL, 
            ldl_cholesterol REAL,
            -- Thyroid Function
            tsh REAL, 
            free_t4 REAL, 
            free_t3 REAL,
            -- Vitamins
            vitamin_d REAL, 
            vitamin_b12 REAL, 
            folate REAL,
            -- Iron Studies
            iron REAL, 
            ferritin REAL, 
            tibc REAL,
            -- Diabetes Markers
            hemoglobin_a1c REAL, 
            insulin REAL,
            -- Other Tests
            uric_acid REAL, 
            crp REAL, 
            esr REAL, 
            psa REAL,
            -- Timestamp
            timestamp TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_user(self, user):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO users (user_id, name, age, sex, height, weight)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (user.user_id, user.name, user.age, user.sex, user.height, user.weight))
        
        conn.commit()
        conn.close()
    
    def get_user(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return User(row[0], row[1], row[2], row[3], row[4], row[5])
        return None
    
    def user_exists(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        conn.close()
        
        return result is not None
    
    def add_lab_results(self, lab_result):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        attributes = [
            'wbc', 'rbc', 'hemoglobin', 'hematocrit', 'platelet_count', 
            'mcv', 'mch', 'mchc', 'rdw', 'mpv',
            'neutrophils', 'lymphocytes', 'monocytes', 'eosinophils', 'basophils',
            'glucose', 'sodium', 'potassium', 'chloride', 'co2',
            'bun', 'creatinine', 'total_protein', 'albumin', 'total_bilirubin', 
            'alkaline_phosphatase', 'alt', 'ast', 'calcium', 'magnesium', 'phosphorus',
            'total_cholesterol', 'triglycerides', 'hdl_cholesterol', 'ldl_cholesterol',
            'tsh', 'free_t4', 'free_t3',
            'vitamin_d', 'vitamin_b12', 'folate',
            'iron', 'ferritin', 'tibc',
            'hemoglobin_a1c', 'insulin', 'uric_acid', 'crp', 'esr', 'psa',
            'timestamp'
        ]
        
        columns = ['user_id'] + attributes
        values = [lab_result.user_id] + [getattr(lab_result, attr, None) for attr in attributes]
        
        placeholders = ', '.join(['?' for _ in values])
        column_names = ', '.join(columns)
        
        query = f'INSERT INTO lab_results ({column_names}) VALUES ({placeholders})'
        cursor.execute(query, values)
        
        conn.commit()
        conn.close()
    
    def get_latest_lab_results(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM lab_results WHERE user_id = ? 
        ORDER BY timestamp DESC LIMIT 1
        ''', (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return LabResult(
                user_id=row[1],
                # CBC
                wbc=row[2], rbc=row[3], hemoglobin=row[4], hematocrit=row[5], platelet_count=row[6],
                mcv=row[7], mch=row[8], mchc=row[9], rdw=row[10], mpv=row[11],
                # CBC Differential
                neutrophils=row[12], lymphocytes=row[13], monocytes=row[14], eosinophils=row[15], 
                basophils=row[16], 
                # Basic Metabolic Panel
                glucose=row[17], sodium=row[18], potassium=row[19], 
                chloride=row[20], co2=row[21], bun=row[22], creatinine=row[23], 
                # Liver Function
                total_protein=row[24], albumin=row[25], total_bilirubin=row[26], 
                alkaline_phosphatase=row[27], alt=row[28], ast=row[29], 
                # Minerals
                calcium=row[30], magnesium=row[31], phosphorus=row[32],
                # Lipid Panel
                total_cholesterol=row[33], triglycerides=row[34], hdl_cholesterol=row[35], 
                ldl_cholesterol=row[36], 
                # Thyroid Function
                tsh=row[37], free_t4=row[38], free_t3=row[39], 
                # Vitamins
                vitamin_d=row[40], vitamin_b12=row[41], folate=row[42], 
                # Iron Studies
                iron=row[43], ferritin=row[44], tibc=row[45], 
                # Diabetes Markers
                hemoglobin_a1c=row[46], insulin=row[47], 
                # Other Tests
                uric_acid=row[48], crp=row[49], esr=row[50], psa=row[51], 
                # Timestamp
                timestamp=row[52]
            )
        return None
    
    def update_lab_results(self, lab_result):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM lab_results WHERE user_id = ?', (lab_result.user_id,))
        conn.commit()
        conn.close()
        
        self.add_lab_results(lab_result)