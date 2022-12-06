class Enemy():

  def __init__(self, name, health):

    self.is_alive = True;
    self.name = name
    self.health = health


class Dragon(Enemy):
  def bite(self):
    bite = self.bite
    print("я кусаюсь")
  def burn(self):
    burn = self.burn
    print("я дышу огнем")
dragon = Dragon("Инхеритий Проворный", 300)

# Не удаляйте код ниже, это проверка!

dragon.bite()
dragon.burn()