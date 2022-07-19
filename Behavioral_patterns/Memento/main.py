from __future__ import annotations


class Doc:

    def __init__(self):
        self.__text = ""
        self.__style = 1

    def add_block(self, text):
        self.__text = text
        print(f"Добавлен блок: {self.__text}")

    def set_style(self, style):
        if self.__style != style:
            self.__style = style
            print(f"Установлен стиль: тип {self.__style}")

    def print(self):
        print(f"\n---Печать---\nСтиль: тип {self.__style}\nТекст:\n{self.__text}\n")

    def save(self) -> DocMemento:
        print("Сохранение документа.")
        return DocMemento(self.__text, self.__style)

    def restore(self, doc_memento: DocMemento):
        print("Откат документа.")
        self.__text = doc_memento.Text
        self.__style = doc_memento.Style


class DocMemento:

    def __init__(self, text, style):
        self.__text = text
        self.__style = style

    @property
    def Text(self):
        return self.__text

    @property
    def Style(self):
        return self.__style


class EditorHistory:

    def __init__(self, doc: Doc) -> None:
        self._doc_mementos = []
        self._doc = doc

    def backup(self) -> None:
        self._doc_mementos.append(self._doc.save())

    def undo(self) -> None:
        if not len(self._doc_mementos):
            return None

        del self._doc_mementos[-1]
        if self._doc_mementos:
            self._doc.restore(self._doc_mementos[-1])
        else:
            print("Невозможно откатить документ.")
            return None

    def show_history(self) -> None:
        print("История изменений:")
        for memento in self._doc_mementos:
            print(f"\nText: {memento.Text}\nStyle: {memento.Style}\n")


if __name__ == '__main__':
    # Инициализация документа и истории редактирования.
    document = Doc()
    history = EditorHistory(document)

    # Первый бекап
    print("----------Первый бекап----------")
    history.backup()
    document.print()
    history.show_history()

    # Первое изменение документа
    print("----------Первое изменение документа----------")
    document.add_block("Hello, world")
    document.set_style(2)

    # Второй бекап
    print("----------Второй бекап----------")
    history.backup()
    document.print()
    history.show_history()

    # Второе изменение документа
    print("----------Второе изменение документа----------")
    document.add_block("What to write after hello world?")
    document.set_style(3)

    # Третий бекап
    print("----------Третий бекап----------")
    history.backup()
    document.print()
    history.show_history()

    # Первый откат
    print("----------Первый откат----------")
    history.undo()
    history.show_history()
    document.print()

    # Второй откат
    print("----------Второй откат----------")
    history.undo()
    history.show_history()
    document.print()
