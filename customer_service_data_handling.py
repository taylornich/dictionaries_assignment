# question 1 task 1

class CustomerServiceData:
    def __init__(self):
        self.customer_tickets = {
            "ticket 001": {"Customer Name": "Jody", "Issue": "Late on payments and seeking late payment options", "Status": "Incomplete"},
            "ticket 002": {"Customer Name": "Rufus", "Issue": "Cannot access account", "Status": "Complete"},
            "ticket 003": {"Customer Name": "Chuck", "Issue": "Needs to update customer information", "Status": "Incomplete"}
        }

        self.new_ticket = 4

    def add_ticket(self, customer, issue):
        ticket_number = f"ticket{self.new_ticket}"
        self.customer_tickets[ticket_number] = {
            "Customer Name": customer,
            "Issue": issue,
            "Status": "Incomplete"
        }
        
        self.new_ticket += 1

    def update_status(self, ticket_number, new_status):
        if ticket_number in self.customer_tickets and new_status in {"Incomplete", "Complete"}:
            self.customer_tickets[ticket_number]["Status"] = new_status

            print(f"ticket '{ticket_number}' successfully updated to '{new_status}'")

        else:
            print("The ticket number or status you have entered is invalid.")

    def display(self, filter_status=None):
        for ticket_number, information in self.customer_tickets.items():
            if filter_status is None or information["Status"] == filter_status:
                print(f"{ticket_number} | {information['Customer Name']} | {information['Issue']} |{information['Status']}")


def main():
    data = CustomerServiceData()

    print("Initial tickets:")
    data.display()

    data.add_ticket("Cass", "Needs password reset")
    data.update_status("ticket 003", "Complete")

    print("\nAll tickets:")
    data.display()

    print("\nIncomplete tickets:")
    data.display(filter_status="Incomplete")

if __name__ == "__main__":
    main()