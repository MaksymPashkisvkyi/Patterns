from __future__ import annotations

from abc import ABC, abstractmethod


class Report:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def get_report(self) -> None:
        self._strategy.output_report('Monthly report', ['Things are going', 'really, really well.'])


class Strategy(ABC):

    @staticmethod
    @abstractmethod
    def output_report(title, text) -> None:
        pass


class ConvertToHTML(Strategy):

    @staticmethod
    def output_report(title, text) -> None:
        print('<html>')
        print(' <head>')
        print(' <title>%s</title>' % title)
        print(' </head>')
        print(' <body>')
        for line in text:
            print(' <p>%s' % line)
        print(' </body>')
        print('</html>')


class ConvertToTxt(Strategy):

    @staticmethod
    def output_report(title, text) -> None:
        print(5 * '*' + title + 5 * '*')
        for line in text:
            print(line)


if __name__ == "__main__":
    report = Report(ConvertToHTML())
    print("Client: Strategy is set to HTML format reporting.")
    report.get_report()
    print()

    print("Client: Strategy is set to Text format reporting.")
    report.strategy = ConvertToTxt()
    report.get_report()
