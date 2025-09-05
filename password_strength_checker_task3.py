import re
import sys
import threading
import time

class PasswordChecker:
    def __init__(self):
        self.password = ""
        self.strength = 0
        self.feedback = []
        self.visible = True 
        
    def set_password(self, password):
        """Set the password to evaluate"""
        self.password = password
        return bool(self.password)
    
    def check_length(self):
        """Check password length and provide feedback"""
        length = len(self.password)
        if length >= 12:
            self.strength += 2
            self.feedback.append("✓ Good password length (12+ characters)")
        elif length >= 8:
            self.strength += 1
            self.feedback.append("✓ Minimum length met (8+ characters)")
        else:
            self.feedback.append("✗ Password too short (min 8 characters required)")
    
    def check_lowercase(self):
        """Check for lowercase letters"""
        if re.search(r'[a-z]', self.password):
            self.strength += 1
            self.feedback.append("✓ Contains lowercase letters")
        else:
            self.feedback.append("✗ Add lowercase letters (a-z)")
    
    def check_uppercase(self):
        """Check for uppercase letters"""
        if re.search(r'[A-Z]', self.password):
            self.strength += 1
            self.feedback.append("✓ Contains uppercase letters (A-Z)")
        else:
            self.feedback.append("✗ Add uppercase letters (A-Z)")
    
    def check_digits(self):
        """Check for digits"""
        if re.search(r'[0-9]', self.password):
            self.strength += 1
            self.feedback.append("✓ Contains numbers (0-9)")
        else:
            self.feedback.append("✗ Add numbers (0-9)")
    
    def check_special_chars(self):
        """Check for special characters"""
        if re.search(r'[^A-Za-z0-9]', self.password):
            self.strength += 1
            self.feedback.append("✓ Contains special characters (!@#$% etc.)")
        else:
            self.feedback.append("✗ Add special characters (!@#$% etc.)")
    
    def check_common_patterns(self):
        """Check for common patterns and weak passwords"""
        common_passwords = {"password", "123456", "qwerty", "letmein", "welcome", "admin", "monkey"}
        
        if self.password.lower() in common_passwords:
            self.strength = 0
            self.feedback.append("✗ This is a very common password - choose something more unique")
            return
            
       
        if re.search(r'(?:123|234|345|456|567|678|789|890|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', self.password.lower()):
            self.strength -= 1
            self.feedback.append("✗ Avoid sequential patterns (e.g., 123, abc)")
        
        
        if re.search(r'(.)\1{2,}', self.password.lower()):
            self.strength -= 1
            self.feedback.append("✗ Avoid repeated characters (e.g., aaa, 111)")
    
    def assess_strength(self):
        """Assess overall password strength"""
        if self.strength <= 2:
            return "Very Weak", "🔴"
        elif self.strength == 3:
            return "Weak", "🟠"
        elif self.strength == 4:
            return "Medium", "🟡"
        elif self.strength == 5:
            return "Strong", "🟢"
        else:
            return "Very Strong", "✅"
    
    def generate_suggestions(self):
        """Generate suggestions based on password assessment"""
        suggestions = []
        
        if self.strength <= 3:
            suggestions.append("• Consider using a passphrase instead of a password")
            suggestions.append("• Use a mix of character types (upper, lower, numbers, symbols)")
            suggestions.append("• Make it at least 12 characters long")
        elif self.strength == 4:
            suggestions.append("• Increase length to 12+ characters for better security")
            suggestions.append("• Add more special characters")
        else:
            suggestions.append("• Your password is strong! Consider using a password manager to keep it secure")
        
        return suggestions
    
    def evaluate(self, password=None):
        """Evaluate the password strength"""
        if password:
            self.password = password
        
       
        self.strength = 0
        self.feedback = []
        
        
        self.check_length()
        self.check_lowercase()
        self.check_uppercase()
        self.check_digits()
        self.check_special_chars()
        self.check_common_patterns()
        
       
        self.strength = max(0, self.strength)
        
       
        strength_rating, strength_icon = self.assess_strength()
        
       
        print("\n" + "="*60)
        print("PASSWORD STRENGTH ANALYSIS")
        print("="*60)
        print(f"Password: {self.password if self.visible else '*' * len(self.password)}")
        print(f"Strength: {strength_icon} {strength_rating} ({self.strength}/6 points)")
        print("\nDETAILED FEEDBACK:")
        for item in self.feedback:
            print(f"  {item}")
        
        
        print("\nSUGGESTIONS:")
        for suggestion in self.generate_suggestions():
            print(f"  {suggestion}")
        
        print("="*60)
        return strength_rating

def get_input_with_echo(prompt, visible=True):
    """Get input with optional echo"""
    print(prompt, end='', flush=True)
    input_str = ""
    
    while True:
        char = getchar()
        if char == '\r' or char == '\n':  
            print()
            break
        elif ord(char) == 127: 
            if len(input_str) > 0:
                input_str = input_str[:-1]
                sys.stdout.write('\b \b')  
                sys.stdout.flush()
        elif ord(char) == 3:  
            raise KeyboardInterrupt
        else:
            input_str += char
            if visible:
                sys.stdout.write(char)
            else:
                sys.stdout.write('*')
            sys.stdout.flush()
    
    return input_str


try:
    import msvcrt
    def getchar():
        """Get a single character on Windows"""
        return msvcrt.getch().decode('utf-8')
except ImportError:
    import tty
    import termios
    def getchar():
        """Get a single character on Unix"""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def animate_loading(message="Evaluating"):
    """Show a simple loading animation"""
    def run():
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        i = 0
        while not loading_stop:
            sys.stdout.write(f"\r{message} {chars[i % len(chars)]}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")
        sys.stdout.flush()
    
    global loading_stop
    loading_stop = False
    t = threading.Thread(target=run)
    t.start()
    return t

def stop_loading(thread):
    """Stop the loading animation"""
    global loading_stop
    loading_stop = True
    thread.join()

def main():
    """Main function to run the password checker"""
    checker = PasswordChecker()
    
    print("🔐 PASSWORD COMPLEXITY CHECKER")
    print("This tool will assess your password strength without storing it.")
    print()
    
   
    examples = {
        "Very Weak": "pass",
        "Weak": "password1",
        "Medium": "Password1",
        "Strong": "Password123!",
        "Very Strong": "CorrectHorseBatteryStaple123!"
    }
    
    while True:
        print("\nOptions:")
        print("1. Check your password (visible)")
        print("2. Check your password (hidden)")
        print("3. View strength examples")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            checker.visible = True
            password = get_input_with_echo("Enter your password (visible): ", visible=True)
            if password:
                loading_thread = animate_loading()
                checker.evaluate(password)
                stop_loading(loading_thread)
            else:
                print("No password entered!")
        elif choice == "2":
            checker.visible = False
            password = get_input_with_echo("Enter your password (hidden): ", visible=False)
            if password:
                loading_thread = animate_loading()
                checker.evaluate(password)
                stop_loading(loading_thread)
            else:
                print("No password entered!")
        elif choice == "3":
            print("\nPassword Strength Examples:")
            for strength, example in examples.items():
                print(f"\n{strength}: {example}")
                checker.visible = True
                checker.evaluate(example)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
