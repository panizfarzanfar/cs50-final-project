import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

class ReadingTimeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reading Time Calculator")
        self.root.geometry("500x500")

        self.text = ""  # برای نگهداری متن PDF استخراج‌شده
        self.speed_dict = {"slow": 100, "average": 200, "fast": 300}

        # ایجاد رابط کاربری
        self.create_widgets()

    def create_widgets(self):
        # عنوان برنامه
        title_label = tk.Label(self.root, text="Reading Time Calculator", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # ناحیه نمایش نتایج
        self.result_text = tk.StringVar()
        result_label = tk.Label(self.root, textvariable=self.result_text, font=("Arial", 12), justify="left")
        result_label.pack(pady=10)

        # دکمه برای انتخاب فایل و محاسبه زمان مطالعه
        select_button = tk.Button(self.root, text="Select PDF File", command=self.calculate_reading_time, font=("Arial", 12))
        select_button.pack(pady=20)

    def extract_text_from_pdf(self, file_path):
        """این تابع متن را از فایل PDF استخراج می‌کند."""
        try:
            with open(file_path, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""  # اگر متنی وجود نداشت، یک رشته خالی قرار می‌دهیم
                return text
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read the PDF file: {e}")
            return ""

    def calculate_reading_time(self):
        """این تابع فایل PDF را پردازش کرده و زمان مطالعه را محاسبه می‌کند."""
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if not file_path:
            return  # اگر کاربر هیچ فایلی انتخاب نکرد، تابع را متوقف کن

        if not file_path.lower().endswith(".pdf"):
            messagebox.showerror("Invalid File", "Please select a valid PDF file.")
            return

        # استخراج متن از PDF
        self.text = self.extract_text_from_pdf(file_path)
        if not self.text.strip():
            messagebox.showinfo("No Text", "The PDF file contains no readable text.")
            return

        # شمارش تعداد کلمات و محاسبه زمان مطالعه
        word_count = len(self.text.split())
        slow_time, stime_h, stime_m = self.calculate_time(word_count, "slow")
        average_time, atime_h, atime_m = self.calculate_time(word_count, "average")
        fast_time, ftime_h, ftime_m = self.calculate_time(word_count, "fast")

        # نمایش نتایج
        self.result_text.set(
            f"Word count: {word_count}\n"
            f"Reading time (slow): {self.format_time(slow_time, stime_h, stime_m)}\n"
            f"Reading time (average): {self.format_time(average_time, atime_h, atime_m)}\n"
            f"Reading time (fast): {self.format_time(fast_time, ftime_h, ftime_m)}"
        )

        self.show_speed_buttons()

    def calculate_time(self, word_count, speed):
        """این تابع زمان خواندن را بر اساس تعداد کلمات و سرعت انتخاب‌شده محاسبه می‌کند."""
        speed_value = self.speed_dict.get(speed, 200)
        time_in_minutes = word_count / speed_value
        hours = int(time_in_minutes // 60)
        minutes = int(time_in_minutes % 60)
        return time_in_minutes, hours, minutes

    def format_time(self, time_in_minutes, hour, min):
        """این تابع زمان را به فرمت ساعت و دقیقه تبدیل می‌کند."""
        minutes = int(time_in_minutes)
        seconds = int((time_in_minutes - minutes) * 60)
        return f"{hour} hour and {min} minutes and {seconds} seconds"

    def show_speed_buttons(self):
        """این تابع دکمه‌ها را برای نمایش متن با سرعت‌های مختلف نمایش می‌دهد."""
        select_button1 = tk.Button(self.root, text="Read Slow Speed!", command=lambda: self.reading_time("slow"), font=("Arial", 12))
        select_button1.pack(pady=10)

        select_button2 = tk.Button(self.root, text="Read Average Speed!", command=lambda: self.reading_time("average"), font=("Arial", 12))
        select_button2.pack(pady=10)

        select_button3 = tk.Button(self.root, text="Read Fast Speed!", command=lambda: self.reading_time("fast"), font=("Arial", 12))
        select_button3.pack(pady=10)

    def reading_time(self, speed):
        """این تابع متن را با توجه به سرعت انتخاب‌شده نمایش می‌دهد."""
        if not self.result_text.get():
            messagebox.showwarning("No Text", "Please calculate reading time first.")
            return
        
        selected_speed = self.speed_dict.get(speed, 200)
        words = self.text.split()  # تبدیل متن به لیست کلمات
        delay = 60 / selected_speed  # تاخیر بین هر کلمه بر اساس سرعت

        # ایجاد پنجره جدید
        reading_window = tk.Toplevel(self.root)
        reading_window.title(f"Reading - {speed.capitalize()} Speed")
        reading_window.geometry("600x400")
        
        # برچسب برای نمایش متن
        reading_label = tk.Label(reading_window, text="", font=("Arial", 14), wraplength=580, justify="left")
        reading_label.pack(pady=20)
        
        def display_words(index=0):
            """نمایش کلمات به ترتیب"""
            if index < len(words):
                reading_label.config(text=" ".join(words[:index + 1]))
                reading_window.after(int(delay * 1000), display_words, index + 1)
            else:
                messagebox.showinfo("Finished", "Reading complete!")

        display_words()  # شروع نمایش کلمات


# ایجاد و راه‌اندازی رابط کاربری
root = tk.Tk()
app = ReadingTimeCalculatorApp(root)
root.mainloop()
