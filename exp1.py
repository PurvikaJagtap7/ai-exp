class VacuumEnvironment:
    def __init__(self):
        # Environment: Two rooms A and B
        self.rooms = {'A': 'dirty', 'B': 'dirty'}
        self.agent_location = 'A'
    
    def is_dirty(self, location):
        return self.rooms[location] == 'dirty'
    
    def clean_room(self, location):
        self.rooms[location] = 'clean'
    
    def move_agent(self, new_location):
        self.agent_location = new_location
    
    def display_state(self):
        print(f"Agent at: {self.agent_location}")
        print(f"Room A: {self.rooms['A']}, Room B: {self.rooms['B']}")

class VacuumAgent:
    def __init__(self, environment):
        self.env = environment
        self.actions_taken = []
    
    def vacuum_agent_function(self):
        """PEAS Implementation"""
        location = self.env.agent_location
        status = self.env.rooms[location]
        
        # Agent decision logic
        if status == 'dirty':
            self.env.clean_room(location)
            action = 'Suck'
        elif location == 'A':
            self.env.move_agent('B')
            action = 'Right'
        elif location == 'B':
            self.env.move_agent('A')
            action = 'Left'
        else:
            action = 'Idle'
        
        self.actions_taken.append(action)
        return action
    
    def run_agent(self):
        step = 0
        while not self.is_goal_reached():
            print(f"\nStep {step + 1}:")
            self.env.display_state()
            action = self.vacuum_agent_function()
            print(f"Action: {action}")
            step += 1
            
            if step > 10:  # Safety check
                break
        
        print("\nFinal State:")
        self.env.display_state()
        print(f"Actions taken: {self.actions_taken}")
    
    def is_goal_reached(self):
        return all(status == 'clean' for status in self.env.rooms.values())

# Usage
if __name__ == "__main__":
    env = VacuumEnvironment()
    agent = VacuumAgent(env)
    agent.run_agent()