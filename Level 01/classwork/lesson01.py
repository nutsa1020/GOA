name = "Nutsa"
# name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "Nutsa" არის ცვლადისთვის მნიშვნელობა
surname = "Macharashvili"

print(name)
# პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

# name = "Macharashvili" ეს არის str(string) ტიპის ცვლადი
# სტრინგი არის ბრჭყალებში მოქცუელი სიმბოლოები
age = 15 # ეს არის int(integer) ტიპის ცვლადი (მთელი რიცხვი)
height = 1.70 # ეს არის float ტიპის ცვლადი (ათწილადი)

knows_programmig = True # True or False, Boolean ტიპის ცვლადი

print(name + " " + surname)

# print(type(age)) age გადაეცა type ფუნქციას, რომელმაც დააბრუნა მისი ტიპი
# და დაბრუნებული ნებისმიერი სიტყვა დავპრინტეთ, რომელმაც გაგვაგებინა, რომ
# print(type(age)) - ის ტიპი არის int(integer) მთელი რიცხვი

print(type(age))
print(type(name))
print(type(surname))
print(type(height))
print(type(knows_programmig))