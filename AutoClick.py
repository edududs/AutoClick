import time
import keyboard
import pyautogui


class AutoClicker:
    def __init__(self, clicks_per_second=100, keyboard_key="F7"):
        self.clicks_per_second = self.transform_data(clicks_per_second)
        self.keyboard_key = keyboard_key
        self.active = False

    def toggle_click(self):
        self.active = not self.active
        if self.active:
            print("AutoClicker activated")
        else:
            print("AutoClicker deactivated")

    def run(self):
        print(f"Pressione '{self.keyboard_key}' para iniciar/parar o autoclicker.")
        print("Pressione 'q' para sair.")

        keyboard.add_hotkey(self.keyboard_key, self.toggle_click)

        while True:
            if self.active:
                pyautogui.click()
                time.sleep(0.00001)
            if keyboard.is_pressed("q"):
                break

    @staticmethod
    def transform_data(clicks_per_second):
        try:
            clicks_per_second = float(clicks_per_second)
        except ValueError:
            return 20.0  # Valor padrão se a conversão falhar
        return max(0.05, clicks_per_second)  # Garantir que não seja menor que 0.05


if __name__ == "__main__":
    print("Runfando")
    clicker = AutoClicker(clicks_per_second=900, keyboard_key="F7")
    clicker.run()
