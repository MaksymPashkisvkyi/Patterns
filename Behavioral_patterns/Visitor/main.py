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
    def hospital_method() -> str:
        return "Hospital"


class School(Organization):

    def accept(self, visitor: Visitor):
        visitor.visit_school(self)

    @staticmethod
    def school_method() -> str:
        return "School"


class Cafe(Organization):

    def accept(self, visitor: Visitor):
        visitor.visit_cafe(self)

    @staticmethod
    def cafe_method() -> str:
        return "Cafe"


class Visitor(ABC):

    @abstractmethod
    def visit_hospital(self, org: Hospital) -> None:
        print()

    @abstractmethod
    def visit_school(self, org: School) -> None:
        pass

    @abstractmethod
    def visit_cafe(self, org: Cafe) -> None:
        pass


class Inspector(Visitor):
    def visit_hospital(self, org) -> None:
        print(f"Inspector visit {org.hospital_method()}.")

    def visit_school(self, org) -> None:
        print(f"Inspector visit {org.school_method()}.")

    def visit_cafe(self, org) -> None:
        print(f"Inspector visit {org.cafe_method()}.")


def client_code(organizations: List[Organization], inspector: Visitor) -> None:
    for organization in organizations:
        organization.accept(inspector)


if __name__ == "__main__":
    organizations = [Hospital(), School(), Cafe()]

    inspector = Inspector()
    client_code(organizations, inspector)

