#!/usr/bin/env python
#
# Thumbtack Problem 2: Simple Database
#
# Utilizes a dictionary for storing data and a list of dictionaries to record
# the database history as changes are made with a transactional block open.  
# This ensures minimal memory is required for each transaction. The time
# complexity for noted operations are:
#     * getting/setting/unsetting in dictionaries is O(1)
#     * checking for a key in a dictionary averages < O(N)
#     * NUMEQUALTO unfortunately appears to be O(N)


class SimpleDatabase:
    def __init__(self):
        self._data = {}
        self._transaction_blocks = []
    
    def set(self, var, value, rollback = False):
        """Sets a value for the given variable in the database, storing the
        previous value in the current transaction block if any blocks are open.
        Since no type information is given, we keep the value as a string."""
        
        # Update the current transactional block if it exists and if a rollback
        # is not currently being performed
        if not rollback and self._transaction_blocks:
            if var in self._data:
                # Record the old variable value only if it is newly changed
                # since beginning the latest transactional block
                if var not in self._transaction_blocks[-1]:
                    self._transaction_blocks[-1][var] = self._data[var]
            else:
                # Record that the value was previously unset
                self._transaction_blocks[-1][var] = None
        
        # Set the value in the database
        if value == None:
            del self._data[var]
        else:
            self._data[var] = value
    
    def get(self, var):
        """Returns the requested variable's value if it exists - otherwise 'NULL'"""
        return self._data[var] if var in self._data else 'NULL'
    
    def unset(self, var):
        """Delete the given variable if it exists in the current transactional block."""
        if var in self._data:
            self.set(var, None)
    
    def numequalto(self, value):
        """Count the number of set variables with the given value."""
        return sum(v == value for v in self._data.values())
    
    def begin(self):
        """Creates a list to store the history of changes to the database."""
        self._transaction_blocks.append({})
    
    def rollback(self):
        """Revert the changes made since beginning the latest transactional block."""
        if self._transaction_blocks:
            for k, v in self._transaction_blocks[-1].items():
                self.set(k, v, rollback = True)
            
            self._transaction_blocks.pop()
        else:
            return 'NO TRANSACTION'
    
    def commit(self):
        """Closes any open transactional blocks, committing the last revisions."""
        self._transaction_blocks = []
            

class DatabaseClient:
    def __init__(self):
        self._database = SimpleDatabase()
    
    def process_command(self, cmd):
        cmd = cmd.split()
        
        # Handle an exit command
        if cmd[0] == 'END':
            return
        
        # Check if command exists, and prevent the user from accessing internal class attributes
        elif '_' not in cmd[0] and hasattr(self._database, cmd[0].lower()):
            f = getattr(self._database, cmd[0].lower())
            
            # Run the given command, returning an error if invalid arguments are given
            try:
                result = f(*cmd[1:])
                
                if result is not None:
                    print(result)
            except Exception as e:
                print('ERROR: MALFORMED COMMAND')
        
        else:
            print('ERROR: INVALID COMMAND')


if __name__ == '__main__':
    import sys
    
    # Initialize the database client
    client = DatabaseClient()
    
    # Read in and process the next command - exit if requested
    cmd = ''
    
    while cmd != 'END':
        cmd = sys.stdin.readline().strip()
        client.process_command(cmd)
