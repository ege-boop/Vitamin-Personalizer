from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, green, black, blue
from datetime import datetime
import os
import platform

class MedicalReportGenerator:
    def __init__(self):
        pass
    
    def generate_pdf_report(self, user, analysis, filename=None):
        try:
            if not user or not analysis:
                return False, "User or analysis data not found"
            
            # Create pdf directory if it doesn't exist
            pdf_dir = "pdf"
            if not os.path.exists(pdf_dir):
                os.makedirs(pdf_dir)
                print(f"Created directory: {pdf_dir}")
            
            if not filename:
                filename = f"Lab_Report_{user.name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
            
            # Save PDF in the pdf directory
            pdf_path = os.path.join(pdf_dir, filename)
            
            c = canvas.Canvas(pdf_path, pagesize=letter)
            width, height = letter
            
            c.setFont("Helvetica-Bold", 18)
            c.drawString(50, height - 50, "LABORATORY ANALYSIS REPORT")
            
            c.setFont("Helvetica", 10)
            c.drawString(450, height - 50, f"Date: {datetime.now().strftime('%B %d, %Y')}")
            c.drawString(450, height - 65, "Vitamin Personalizer System")
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, height - 90, "PATIENT INFORMATION")
            c.line(50, height - 95, 550, height - 95)
            c.setFont("Helvetica", 10)
            c.drawString(50, height - 115, f"Name: {user.name}")
            c.drawString(50, height - 130, f"Patient ID: {user.user_id}")
            c.drawString(50, height - 145, f"Age: {user.age} years")
            c.drawString(250, height - 115, f"Gender: {user.sex}")
            c.drawString(250, height - 130, f"Height: {user.height} cm")
            c.drawString(250, height - 145, f"Weight: {user.weight} kg")
            c.drawString(400, height - 130, f"BMI: {user.bmi:.1f}")
            
            abnormal_results = []
            normal_results = []
            
            for test_name, result in analysis.items():
                if result['status'] != 'Normal':
                    abnormal_results.append((test_name, result))
                else:
                    normal_results.append((test_name, result))
            
            y = height - 180
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, y, "CLINICAL SUMMARY")
            c.line(50, y - 5, 550, y - 5)
            y -= 25
            
            c.setFont("Helvetica", 10)
            total_tests = len(analysis)
            abnormal_count = len(abnormal_results)
            normal_count = len(normal_results)
            
            c.drawString(50, y, f"Total Tests Performed: {total_tests}")
            y -= 15
            c.drawString(50, y, f"Normal Results: {normal_count}")
            y -= 15
            c.drawString(50, y, f"Abnormal Results: {abnormal_count}")
            y -= 30
            if abnormal_results:
                c.setFont("Helvetica-Bold", 12)
                c.drawString(50, y, "ABNORMAL FINDINGS REQUIRING ATTENTION")
                c.line(50, y - 5, 550, y - 5)
                y -= 20
                
                c.setFont("Helvetica-Bold", 9)
                c.drawString(50, y, "Test Name")
                c.drawString(180, y, "Result")
                c.drawString(250, y, "Status")
                c.drawString(320, y, "Recommendation")
                y -= 15
                
                c.setFont("Helvetica", 8)
                for test_name, result in abnormal_results:
                    if y < 100:
                        c.showPage()
                        y = height - 50
                    
                    c.drawString(50, y, test_name)
                    c.drawString(180, y, f"{result['value']} {result['unit']}")
                    
                    if result['status'] == 'High':
                        c.setFillColor(red)
                    elif result['status'] == 'Low':
                        c.setFillColor(blue)
                    
                    c.drawString(250, y, result['status'])
                    c.setFillColor(black)
                    
                    if result['recommendations']:
                        c.drawString(320, y, result['recommendations']['supplement'][:50])
                    
                    y -= 12
                
                y -= 20
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y, "TREATMENT RECOMMENDATIONS")
            c.line(50, y - 5, 550, y - 5)
            y -= 20
            
            supplements_to_take = []
            supplements_to_stop = []
            dietary_changes = []
            
            for test_name, result in abnormal_results:
                if result['recommendations']:
                    if result['status'] == 'Low':
                        supplements_to_take.append(result['recommendations']['supplement'])
                        dietary_changes.append(f"For {test_name}: {result['recommendations']['diet']}")
                    elif result['status'] == 'High':
                        supplements_to_stop.append(result['recommendations']['supplement'])
                        dietary_changes.append(f"For {test_name}: {result['recommendations']['diet']}")
            
            c.setFont("Helvetica-Bold", 10)
            if supplements_to_take:
                c.drawString(50, y, "SUPPLEMENTS TO START:")
                y -= 15
                c.setFont("Helvetica", 9)
                for supplement in supplements_to_take:
                    c.drawString(70, y, f"• {supplement}")
                    y -= 12
                y -= 10
            
            c.setFont("Helvetica-Bold", 10)
            if supplements_to_stop:
                c.drawString(50, y, "SUPPLEMENTS TO REDUCE OR STOP:")
                y -= 15
                c.setFont("Helvetica", 9)
                for supplement in supplements_to_stop:
                    c.drawString(70, y, f"• {supplement}")
                    y -= 12
                y -= 10
            
            c.setFont("Helvetica-Bold", 10)
            if dietary_changes:
                c.drawString(50, y, "DIETARY MODIFICATIONS:")
                y -= 15
                c.setFont("Helvetica", 9)
                for diet in dietary_changes[:5]:
                    c.drawString(70, y, f"• {diet}")
                    y -= 12
                y -= 10
            if normal_results:
                if y < 200:
                    c.showPage()
                    y = height - 50
                
                c.setFont("Helvetica-Bold", 12)
                c.drawString(50, y, "NORMAL RESULTS")
                c.line(50, y - 5, 550, y - 5)
                y -= 20
                
                c.setFont("Helvetica", 8)
                count = 0
                for test_name, result in normal_results:
                    if y < 50:
                        c.showPage()
                        y = height - 50
                    
                    if count % 3 == 0 and count > 0:
                        y -= 12
                    
                    x_pos = 50 + (count % 3) * 170
                    c.drawString(x_pos, y, f"{test_name}: {result['value']} {result['unit']}")
                    count += 1
                    
                    if count % 3 == 0:
                        y -= 12
            c.showPage()
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, height - 50, "IMPORTANT MEDICAL INFORMATION")
            c.line(50, height - 55, 550, height - 55)
            
            c.setFont("Helvetica", 11)
            y = height - 80
            disclaimer = [
                "This report is generated by automated analysis software for educational purposes.",
                "All abnormal values must be reviewed and confirmed by qualified medical professionals.",
                "Do not start, stop, or modify any supplements without consulting your healthcare provider.",
                "This report does not constitute medical advice and should not replace professional consultation.",
                "Please bring this report to your healthcare provider for proper medical interpretation.",
                "Follow-up testing may be required to monitor progress and adjust recommendations."
            ]
            
            for line in disclaimer:
                c.drawString(50, y, line)
                y -= 18
            
            c.setFont("Helvetica", 8)
            c.drawString(50, 30, f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            c.drawString(400, 30, "For medical professional review only")
            
            c.save()
            
            # Try to open automatically
            self._open_pdf(pdf_path)
            
            return True, f"Professional medical report saved as: {pdf_path}"
            
        except ImportError:
            return False, "Please install reportlab: pip install reportlab"
        except Exception as e:
            return False, f"Error creating PDF: {str(e)}"
    
    def _open_pdf(self, filename):
        try:
            if platform.system() == 'Windows':
                os.startfile(filename)
            elif platform.system() == 'Darwin':
                os.system(f'open "{filename}"')
            else:
                os.system(f'xdg-open "{filename}"')
        except:
            pass