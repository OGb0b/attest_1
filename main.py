from collections import deque
class Delivery:
    def __init__(self, track_number, point_of_departure,point_of_destination, weight, time):
        self.track_number = track_number
        self.point_of_departure = point_of_departure
        self.point_of_destination = point_of_destination
        self.weight = weight
        self.time = time

    def __repr__(self):
        return (f'Номер посылки - {self.track_number} \n'
                f'Пункт отправки - {self.point_of_departure} \n'
                f'Пункт назначения - {self.point_of_destination} \n'
                f'Вес - {self.weight} \n'
                f'Время доставки - {self.time}')
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("удаление из пустого стека")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("получение из пустого стека")


    def size(self):
        return len(self.items)


class Company:
    def __init__(self):
        self.deliveries = []
        self.urgent_stack = Stack()
        self.regular_queue = deque()

    def add_delivery(self, arr, priority):
        point_of_departure = arr[1]
        point_of_destination = arr[2]
        try:
            track_number = int(arr[0])
            weight = int(arr[3])
            time = int(arr[4])
        except ValueError:
            print("Ошибка: номер, вес и время должны быть числами.")
            return
        new_delivery = Delivery(track_number, point_of_departure, point_of_destination, weight, time)
        self.deliveries.append(new_delivery)
        if priority == '1':
            self.urgent_stack.push(new_delivery)
        else:
            self.regular_queue.append(new_delivery)

    def display_delivery(self):
        if not self.deliveries:
            print('\nДоставок нет')
            return
        print('\nНа данный момент есть следующие доставки:')
        for deliv in self.deliveries:
            print(deliv)

    def merge_sort_by_weight(self, deliveries=None):
        if deliveries is None:
            deliveries = self.deliveries.copy()
        if len(deliveries) <= 1:
            return deliveries
        mid = len(deliveries) // 2
        left = self.merge_sort_by_weight(deliveries[:mid])
        right = self.merge_sort_by_weight(deliveries[mid:])
        return self.merge(left, right)

    def merge(self,left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].weight < right[j].weight:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        self.deliveries = result
        return self.deliveries

    def quick_sort_by_time(self, deliveries=None):
        if deliveries is None:
            deliveries = self.deliveries
        if len(deliveries) <= 1:
            return deliveries
        pivot = deliveries[len(deliveries)//2].time
        left = [x for x in deliveries if x.time < pivot]
        middle = [x for x in deliveries if x.time == pivot]
        right = [x for x in deliveries if x.time > pivot]
        result = self.quick_sort_by_time(left) + self.quick_sort_by_time(middle) + self.quick_sort_by_time(right)
        self.deliveries = result
        return self.deliveries

    def heapify(self, n, i, deliveries=None):
        if deliveries is None:
            deliveries = self.deliveries.copy()

        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and deliveries[left].track_number > deliveries[largest].track_number:
            largest = left

        if right < n  and deliveries[right].track_number > deliveries[largest].track_number:
            largest = right

        if largest != i:
            deliveries[i], deliveries[largest] = deliveries[largest], deliveries[i]
            self.heapify(n, largest, deliveries)

    def heap_sort(self, deliveries=None):
        if deliveries is None:
            deliveries= self.deliveries.copy()
        n = len(deliveries)
        for i in range(n//2-1, -1, -1):
            self.heapify(n, i, deliveries)
        for i in range(n-1,0,-1):
            deliveries[i], deliveries[0] = deliveries[0], deliveries[i]
            self.heapify(i, 0, deliveries)
        self.deliveries = deliveries
        return self.deliveries

    def linear_search_by_track_number(self, number):
        try:
            number = int(number)
        except ValueError as e:
            print('Неправильный формат введенных данных')
            return
        found = False
        for deliv in self.deliveries:
            if deliv.track_number == number:
                print('Нашлись следующие доставки:')
                print(deliv)
                found = True
        if not found:
            print('Доставка не найдена')

    def binary_search_by_time(self, tm):
        sorted_deliveries = self.quick_sort_by_time(self.deliveries.copy())
        left, right = 0, len(sorted_deliveries) - 1
        found = []
        while left <= right:
            mid = (left + right) // 2
            if sorted_deliveries[mid].time == tm:
                found.append(sorted_deliveries[mid])
                i = mid - 1
                while i >= 0 and sorted_deliveries[i].time == tm:
                    found.append(sorted_deliveries[i])
                    i -= 1
                i = mid + 1
                while i < len(sorted_deliveries) and sorted_deliveries[i].time == tm:
                    found.append(sorted_deliveries[i])
                    i += 1
                break
            elif sorted_deliveries[mid].time < tm:
                left = mid + 1
            else:
                right = mid - 1
        if found:
            print(f"Доставки за время {tm}:")
            for delivery in found:
                print(delivery)
        else:
            print("Доставки не найдены")

    def delete_deliveries(self, track_number):
        try:
            track_number = int(track_number)
        except ValueError as e:
            print('Неправильный формат введенных данных')
            return
        for deliv in self.deliveries:
            if track_number == deliv.track_number():
                self.deliveries.pop(self.deliveries.index(deliv))
                print('Доставка удалена')
def main():
    company = Company()
    while True:
        print('\n1. Показать все доставки')
        print('2. Сортировать доставки по весу')
        print('3. Сортировать доставки по времени')
        print('4. Сортировать доставки по трек номеру')
        print('5. Найти доставки по трек номеру')
        print('6. Найти доставки по времени')
        print('7. Добавить доcтавку')
        print('8. Удалить доставку')
        print('9. Выйти')

        choice = input('Выберите действие: ')
        if choice == '1':
            company.display_delivery()
        elif choice == '2':
            company.merge_sort_by_weight()
        elif choice == '3':
            company.quick_sort_by_time()
        elif choice == '4':
            company.heap_sort()
        elif choice == '5':
            company.linear_search_by_track_number()
        elif choice == '6':
            company.binary_search_by_time()
        elif choice == '7':
            track_number = input('Введите номер доставки: ')
            point_of_departure = input('Введите пункт отправки: ')
            point_of_destination = input('Введите пункт назначения: ')
            weight = input('Введите вес груза: ')
            time = input('Введите время доставки: ')
            priority = input('Введите 1, если заказ срочный, иначе система посчитает его обычным.\n')
            company.add_delivery([track_number, point_of_departure, point_of_destination, weight, time], priority)
        elif choice == '8':
            track_number = input('Введите трек номер доставки: ')
            company.delete_deliveries(track_number)

        elif choice == '9':
            break
        else:
            print('Неверный ввод, попробуйте еще раз')

if __name__ == '__main__':
    main()
