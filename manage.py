def snakes_and_ladders(n, transitions, rolls, final_position):
    # Create a board representation (1-100)
    board = {i: i for i in range(1, 101)}
    
    # Fill in snakes and ladders
    for start, end in transitions:
        board[start] = end
    
    # Function to simulate movement on the board
    def simulate(start):
        position = start
        for roll in rolls:
            position += roll
            if position > 100:
                position = 100  # Can't exceed position 100
            position = board[position]  # Move according to snake or ladder
        return position
    
    # Check if final_position is reachable without any switch
    if simulate(1) == final_position:
        return "Not affected"
    
    # Try switching each snake/ladder
    for start, end in transitions:
        # Switch snake to ladder: Remove snake and add ladder
        original_destination = board[start]  # Save original destination for start
        board[start] = start  # Remove the snake at 'start'
        board[end] = start    # Add a ladder from 'start' to 'end'
        
        if simulate(1) == final_position:
            return f"Ladder {start} {end}"
        
        # Restore original state
        board[start] = original_destination
        board[end] = end  # Restore original state for the ladder
        
        # Switch ladder to snake: Remove ladder and add snake
        board[end] = end    # Remove the ladder at 'end'
        board[start] = end  # Add a snake from 'start' to 'end'
        
        if simulate(1) == final_position:
            return f"Snake {end} {start}"
        
        # Restore original state again
        board[start] = original_destination
        board[end] = end
    
    # If no switch works, the position is not reachable
    return "Not reachable"

def main():
    # Input number of snakes and ladders
    n = int(input())
    
    transitions = []
    for _ in range(n):
        start, end = map(int, input().split())
        transitions.append((start, end))
    
    rolls = list(map(int, input().split()))
    final_position = int(input())
    
    result = snakes_and_ladders(n, transitions, rolls, final_position)
    print(result)

if _name_ == "_main_":
    main()