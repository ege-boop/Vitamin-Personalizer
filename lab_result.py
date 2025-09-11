class LabResult:
    def __init__(self, user_id, wbc=None, rbc=None, hemoglobin=None, hematocrit=None, 
                 platelet_count=None, mcv=None, mch=None, mchc=None, rdw=None, mpv=None,
                 neutrophils=None, lymphocytes=None, monocytes=None, eosinophils=None, 
                 basophils=None, glucose=None, sodium=None, potassium=None, chloride=None, 
                 co2=None, bun=None, creatinine=None, total_protein=None, albumin=None, 
                 total_bilirubin=None, alkaline_phosphatase=None, alt=None, ast=None, 
                 calcium=None, total_cholesterol=None, triglycerides=None, hdl_cholesterol=None, 
                 ldl_cholesterol=None, tsh=None, free_t4=None, free_t3=None, vitamin_d=None, 
                 vitamin_b12=None, folate=None, iron=None, ferritin=None, tibc=None, 
                 hemoglobin_a1c=None, insulin=None, uric_acid=None, crp=None, esr=None, 
                 psa=None, magnesium=None, phosphorus=None, timestamp=None):
        self.user_id = user_id
        self.wbc = wbc
        self.rbc = rbc
        self.hemoglobin = hemoglobin
        self.hematocrit = hematocrit
        self.platelet_count = platelet_count
        self.mcv = mcv
        self.mch = mch
        self.mchc = mchc
        self.rdw = rdw
        self.mpv = mpv
        self.neutrophils = neutrophils
        self.lymphocytes = lymphocytes
        self.monocytes = monocytes
        self.eosinophils = eosinophils
        self.basophils = basophils
        self.glucose = glucose
        self.sodium = sodium
        self.potassium = potassium
        self.chloride = chloride
        self.co2 = co2
        self.bun = bun
        self.creatinine = creatinine
        self.total_protein = total_protein
        self.albumin = albumin
        self.total_bilirubin = total_bilirubin
        self.alkaline_phosphatase = alkaline_phosphatase
        self.alt = alt
        self.ast = ast
        self.calcium = calcium
        self.total_cholesterol = total_cholesterol
        self.triglycerides = triglycerides
        self.hdl_cholesterol = hdl_cholesterol
        self.ldl_cholesterol = ldl_cholesterol
        self.tsh = tsh
        self.free_t4 = free_t4
        self.free_t3 = free_t3
        self.vitamin_d = vitamin_d
        self.vitamin_b12 = vitamin_b12
        self.folate = folate
        self.iron = iron
        self.ferritin = ferritin
        self.tibc = tibc
        self.hemoglobin_a1c = hemoglobin_a1c
        self.insulin = insulin
        self.uric_acid = uric_acid
        self.crp = crp
        self.esr = esr
        self.psa = psa
        self.magnesium = magnesium
        self.phosphorus = phosphorus
        self.timestamp = timestamp