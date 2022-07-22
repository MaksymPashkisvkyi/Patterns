from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Organization(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class Hospital(Organization):

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_hospital(self)

    @staticmethod
    def exclusive_method_of_concrete_component_a() -> str:
        return "A"


class School(Organization):

    def accept(self, visitor: Visitor):
        visitor.visit_school(self)

    @staticmethod
    def special_method_of_concrete_component_b() -> str:
        return "B"


class Cafe(Organization):

    def accept(self, visitor: Visitor):
        visitor.visit_cafe(self)

    @staticmethod
    def special_method_of_concrete_component_b() -> str:
        return "B"


class Visitor(ABC):

    @abstractmethod
    def visit_hospital(self, element: Hospital) -> None:
        pass

    @abstractmethod
    def visit_school(self, element: School) -> None:
        pass

    @abstractmethod
    def visit_cafe(self, element: Cafe) -> None:
        pass


class Inspector(Visitor):
    def visit_hospital(self, element: Hospital) -> None:
        print("Inspector visit hospital.")

    def visit_school(self, element: School) -> None:
        print("Inspector visit school.")

    def visit_cafe(self, element: Cafe) -> None:
        print("Inspector visit cafe.")


def client_code(organizations: List[Organization], inspector: Visitor) -> None:
    for organization in organizations:
        organization.accept(inspector)


if __name__ == "__main__":
    organizations = [Hospital(), School(), Cafe()]

    print("The client code works with all visitors via the base Visitor interface:")
    inspector = Inspector()
    client_code(organizations, inspector)

