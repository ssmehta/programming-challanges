#!/usr/bin/python

import re, sys


class Transaction:
    states = {'il': 'illinois', 'ca': 'california', 'ny': 'new york'}
    
    def __init__(self, order_id, deal_id, email, address, city, state, zip_code, cc):
        self.order_id = int(order_id)
        self.deal_id = int(deal_id)
        
        self.email = self.clean_email(email)
        self.address = self.clean_address(address)
        self.city = self.clean_city(city)
        self.state = self.clean_state(state)
        self.zip_code = self.clean_zip_code(zip_code)
        self.cc = self.clean_cc(cc)
    
    def __repr__(self):
        return("Transaction: order = %d, deal = %d; Customer: %s, %s, %s, %s, %d, %d" % (self.order_id, self.deal_id, self.email, self.address, self.city, self.state, self.zip_code, self.cc))
    
    def is_fraudulent_match(self, t):
        return(self.deal_id == t.deal_id and self.cc != t.cc and (
            self.email == t.email or (self.address == t.address and self.city == t.city and self.state == t.state and self.zip_code == t.zip_code)
        ))
    
    
    @staticmethod
    def clean_email(email):
        username, domain = email.lower().split('@')
        return(username.replace('.', '').split('+')[0] +'@'+ domain)
    
    @staticmethod
    def clean_address(address):
        return(address.lower().replace('st.', 'street').replace('rd.', 'road').replace('.', ''))
    
    @staticmethod
    def clean_city(city):
        return(city.lower())
    
    @staticmethod
    def clean_state(state):
        return(Transaction.states[state.lower()] if state.lower() in Transaction.states else state.lower())
    
    @staticmethod
    def clean_zip_code(zip_code):
        return(int(zip_code.split('-')[0]))
    
    @staticmethod
    def clean_cc(cc):
        return(int(cc.replace(' ', '').replace('-', '')))


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    # Improve efficiency by sorting by deal_id
    transactions = {}
    
    for i in range(N):
        t = Transaction(*sys.stdin.readline().strip().split(','))
        
        if t.deal_id not in transactions:
            transactions[t.deal_id] = []
        transactions[t.deal_id].append(t)
    
    
    # Find fraudulent transactions
    fraudulent_transactions = []
    
    for k, v in transactions.items():
        for i in range(len(v) - 1):
            for j in range(i + 1, len(v)):
                if v[i].is_fraudulent_match(v[j]):
                    fraudulent_transactions.append(v[i].order_id)
                    fraudulent_transactions.append(v[j].order_id)
    
    print(','.join(map(str, sorted(set(fraudulent_transactions)))))
