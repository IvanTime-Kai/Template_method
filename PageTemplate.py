# import module ABC ( Abstract Base Classes ) để cung cấp Abstract class, module abstractmethod để khai báo phương thức trừu tượng

from abc import ABC, abstractmethod

# Khai báo đây là lớp trừu tượng
class PageTemplate(ABC):
    def ShowHeader(self):
        print('Header')
    def ShowFooter(self):
        print('Footer')

    # từ khoá khai báo phương thức trừ tượng
    @abstractmethod
    def ShowBody(self):
        pass;
    def Template_Method(self):
        self.ShowHeader();
        self.ShowBody();
        self.ShowFooter();