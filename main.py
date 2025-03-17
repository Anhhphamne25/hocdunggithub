import os
import sys
 def main():
    """Hàm chính để chạy ứng dụng Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    #Đặt biến môi trường chỉ định file cấu hình của Django
    
    try:
    	form django.core.management import execute_from_command_line
        #Import hàm chạy lệnh django
        except ImportError as exc:
            raise ImportError(
            	"Không thể import Django. Hãy kiểm tra xem Django đã được cài đặt chưa."
                ) form exc
                
      execute_from_command_line(sys.argv)
    	# Chạy lệnh từ terminal (ví dụ: 'python main.py runserver')
        
        if __name_-== "__main__":
            main()
            
            