class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.tickets = {}
        self.movie_counter = 1
        self.user_counter = 1
        self.ticket_counter = 1

    def addMovie(self, movieName):
        movie_id = self.movie_counter
        self.movies[movie_id] = movieName
        self.movie_counter += 1
        return movie_id

    def showAllMovies(self):
        for movie_id, movie_name in self.movies.items():
            print(f"{movie_id}. {movie_name}")

    def addUser(self, userName):
        user_id = self.user_counter
        self.users[user_id] = userName
        self.user_counter += 1
        return user_id

    def buyTicket(self, userId, movieId):
        if userId in self.users and movieId in self.movies:
            ticket_id = self.ticket_counter
            self.tickets[ticket_id] = (userId, movieId)
            self.ticket_counter += 1
            return ticket_id
        return None

    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:
            del self.tickets[ticketId]
            return True
        return False

def main():
    cinemaSystem = CinemaTicketSystem()
    while True:
        print("������������, � ��� ���� ��������� ��������� �������:")
        print("1. �������� ����� �����")
        print("2. �������� ��� ��������� ������")
        print("3. �������� ������ ������������")
        print("4. ������ �����")
        print("5. �������� ������� ������")
        print("0. �����")
        choice = input("�������� ��������: ")
        
        if choice == "1":
            movie_name = input("������� �������� ������: ")
            movie_id = cinemaSystem.addMovie(movie_name)
            print(f"����� �������� � ��������������� {movie_id}.")
        
        elif choice == "2":
            cinemaSystem.showAllMovies()
        
        elif choice == "3":
            user_name = input("������� ��� ������������: ")
            user_id = cinemaSystem.addUser(user_name)
            print(f"������������ �������� � ��������������� {user_id}.")
        
        elif choice == "4":
            user_id = int(input("������� ������������� ������������: "))
            movie_id = int(input("������� ������������� ������: "))
            ticket_id = cinemaSystem.buyTicket(user_id, movie_id)
            if ticket_id:
                print(f"����� ������ � ��������������� {ticket_id}.")
            else:
                print("������ ��� ������� ������.")
        
        elif choice == "5":
            ticket_id = int(input("������� ������������� ������: "))
            if cinemaSystem.cancelTicket(ticket_id):
                print("����� ������� �������.")
            else:
                print("����� � ����� ��������������� �� ������.")
        
        elif choice == "0":
            print("�����.")
            break
        
        else:
            print("�������� �����. ���������� �����.")

if __name__ == "__main__":
    main()
