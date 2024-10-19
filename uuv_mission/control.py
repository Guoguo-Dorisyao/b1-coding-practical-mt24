class PDController:
    def __init__(self, KP: float = 0.15, KD: float = 0.6):
        self.KP = KP
        self.KD = KD
        self.previous_error = 0.0

    def control(self, reference: float, output: float) -> float:
        error = reference - output
        derivative = error - self.previous_error
        control_action = self.KP * error + self.KD * derivative
        self.previous_error = error
        return control_action

# Example usage:
# pd_controller = PDController()
# control_action = pd_controller.control(reference_value, output_value)