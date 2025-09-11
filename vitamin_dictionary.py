import webbrowser

class VitaminDictionary:
    def __init__(self):
        self.main_website = 'https://ods.od.nih.gov/factsheets/list-all/'
    
    def show_all_vitamins(self):
        print("\n" + "="*60)
        print("          VITAMIN & MINERAL DICTIONARY")
        print("="*60)
        print("Opening comprehensive vitamin database...")
        print("Source: NIH Office of Dietary Supplements")
        
        try:
            webbrowser.open(self.main_website)
            print("Website opened in your browser!")
        except:
            print("Could not open browser automatically.")
            print(f"Please visit: {self.main_website}")
        
        print("\nThis website contains:")
        print("- All vitamins and minerals information")
        print("- Recommended daily amounts")
        print("- Food sources and supplements")
        print("- Health benefits and risks")
        print("- Scientific research references")
        print("- Search function to find specific nutrients")
    
    def search_vitamin(self, vitamin_name):
        return True