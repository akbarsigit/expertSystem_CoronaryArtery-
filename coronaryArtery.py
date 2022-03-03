# Nama : Akbar Sigit Putra
# NIM  : 20/463590/TK/51582
# Prodi : Teknologi Informasi

from experta import *

class CoronaryArteryDiagnosis(KnowledgeEngine):

########################################

    @Rule(salience = 99)
    def user_question(self):
        print("Please answer the question below to diagnose your risk of getting coronary heart disease\n\n")
        self.old_age = input("Are you older than 32? (y/n)\n")
        self.declare(Fact(adultAge = self.old_age))
        self.high_heart_rate = input("\nAre your heart rate grater than 99.5 bpm? (y/n)\n")
        self.declare(Fact(high_heart_rate = self.high_heart_rate))
        self.high_blood_preasure = input("\nAre your blood preasure greater than 152.5 mmHg? (y/n)\n")
        self.declare(Fact(high_blood_preasure = self.high_blood_preasure))
        self.high_triglyceride = input("\nDo you have high triglyceride (Triglyceride > 315.5 mg/dL)? (y/n)\n")
        self.declare(Fact(high_triglyceride = self.high_triglyceride))
        self.high_creatinine  = input("\nDo you have high creatinine (Creatinine > 1.52 mg/dL)? (y/n)\n")
        self.declare(Fact(high_creatinine  = self.high_creatinine ))
        self.high_glucose = input("\nDo you have high blood sugar (Glucose > 69.5 mg/dL) ? (y/n)\n")
        self.declare(Fact(high_glucose = self.high_glucose))
        self.chest_pain = input("\nDo you suffer chest pain? (y/n)\n")
        self.declare(Fact(chest_pain = self.chest_pain))


########################################

    # Very High Diagnose Rule
    @Rule(Fact(adultAge = 'y'), Fact(high_heart_rate = 'y'), Fact(high_blood_preasure = 'y'),Fact(high_glucose = 'y'),Fact(high_triglyceride = 'y'),
    Fact(high_creatinine = 'y'),Fact(chest_pain = 'y'))
    def diagnose1(self):
        print("\n\nYou have a VERY HIGH chance of having coronary artery disease")
        self.declare(Fact(indication = True))

    @Rule(Fact(adultAge = 'y'), Fact(high_heart_rate = 'y'), Fact(high_blood_preasure = 'y'),Fact(high_glucose = 'y'),Fact(high_triglyceride = 'n'),
    Fact(high_creatinine = 'n'),Fact(chest_pain = 'n'))
    def diagnose2(self):
        print("\n\nYou have a VERY HIGH chance of having coronary artery disease")
        self.declare(Fact(indication = True))


    # High Diagnose Rule
    @Rule(Fact(adultAge = 'y'), Fact(high_heart_rate = 'y'), Fact(high_blood_preasure = 'n'),Fact(high_glucose = 'n'),Fact(high_triglyceride = 'y'),
    Fact(high_creatinine = 'y'),Fact(chest_pain = 'y'))
    def diagnose3(self):
        print("\n\nYou have a HIGH chance of having coronary artery disease")
        self.declare(Fact(indication = True))
  
    @Rule(Fact(adultAge = 'y'), Fact(high_heart_rate = 'n'), Fact(high_blood_preasure = 'n'),Fact(high_glucose = 'y'),Fact(high_triglyceride = 'y'),
    Fact(high_creatinine = 'y'),Fact(chest_pain = 'y'))
    def diagnose4(self):
        print("\n\nYou have a HIGH chance of having coronary artery disease")
        self.declare(Fact(indication = True))


    # Moderate Diagnose Rule
    @Rule(Fact(adultAge = 'n'), Fact(high_heart_rate = 'y'), Fact(high_blood_preasure = 'n'),Fact(high_glucose = 'y'),Fact(high_triglyceride = 'y'),
    Fact(high_creatinine = 'y'),Fact(chest_pain = 'n'))
    def diagnose5(self):
        print("\n\nYou have a MODERATE chance of having coronary artery disease")
        self.declare(Fact(indication = True))

    @Rule(Fact(adultAge = 'y'), Fact(high_heart_rate = 'n'), Fact(high_blood_preasure = 'y'),Fact(high_glucose = 'n'),Fact(high_triglyceride = 'y'),
    Fact(high_creatinine = 'y'),Fact(chest_pain = 'y'))
    def diagnose6(self):
        print("\n\nYou have a MODERATE chance of having coronary artery disease")
        self.declare(Fact(indication = True))

    @Rule(Fact(adultAge = 'n'), Fact(high_heart_rate = 'n'), Fact(high_blood_preasure = 'y'),Fact(high_glucose = 'y'),Fact(high_triglyceride = 'y'),
    Fact(high_creatinine = 'y'),Fact(chest_pain = 'n'))
    def diagnose7(self):
        print("\n\nYou have a MODERATE chance of having coronary artery disease")
        self.declare(Fact(indication = True))


    #Mild Diagnose Rule
    @Rule(Fact(adultAge = 'y'), Fact(high_heart_rate = 'y'), Fact(high_blood_preasure = 'n'),Fact(high_glucose = 'y'),Fact(high_triglyceride = 'y'),
    Fact(high_creatinine = 'y'),Fact(chest_pain = 'n'))
    def diagnose8(self):
        print("\n\nYou have a MILD chance of having coronary artery disease")
        self.declare(Fact(indication = True))

    @Rule(Fact(adultAge = 'n'), Fact(high_heart_rate = 'n'), Fact(high_blood_preasure = 'n'),Fact(high_glucose = 'n'),Fact(high_triglyceride = 'y'),
    Fact(high_creatinine = 'n'),Fact(chest_pain = 'y'))
    def diagnose9(self):
        print("\n\nYou have a MILD chance of having coronary artery disease")
        self.declare(Fact(indication = True))

    
    #Healthy Diagnose Rule

    @Rule(OR(Fact(adultAge = 'y'),Fact(adultAge = 'n')), Fact(high_heart_rate = 'n'), Fact(high_blood_preasure = 'n'),Fact(high_glucose = 'n'),Fact(high_triglyceride = 'n'),
    Fact(high_creatinine = 'n'),Fact(chest_pain = 'n'))
    def diagnose10(self):
        print("\n\nYoure Healthy")
        self.declare(Fact(indication = True))


    @Rule(NOT (Fact(indication = W())))
    def diagnose11(self):
        print("\n\nSorry, our system are not confident enough to diagnose your disease. We recommend that you go to the doctor")


if __name__ == "__main__":
    engine = CoronaryArteryDiagnosis()
    engine.reset()
    engine.run()
   