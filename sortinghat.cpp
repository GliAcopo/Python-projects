#include <iostream>
#include <windows.h>
// points
int gryffindor = 0;
int hufflepuff = 0;
int ravenclaw = 0;
int slytherin = 0;
int max = 0;

//answers
int answer1;
int answer2;
int answer3;
int answer4;
std::string house;

int main(){

  std::cout << "You have now started the sorting hat quiz!\n(use numbers to respond)\n";

  //question1
  std::cout << "Q1) When I'm dead, I want people to remember me as: \n\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n";
  std::cin >> answer1;
  //logic1
  if (answer1 == 1)
    hufflepuff += 1;
  else if (answer1 == 2)
    slytherin += 1;
  else if (answer1 == 3)
    ravenclaw += 1;
  else if (answer1 == 4)
    gryffindor += 1;
  else
    std::cout << "Invalid input\n";

 //question2
 std::cout << "Q2) Dawn or Dusk?\n1) Dawn\n2) Dusk\n";
 std::cin >> answer2;
 //logic2
 if (answer2 == 1)
    (gryffindor += 1) and (ravenclaw += 1);
  else if (answer2 == 2)
    (slytherin += 1) and (hufflepuff += 1);
  else
    std::cout << "Invalid input\n";

  //question3
  std::cout << "Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n";
  std::cin >> answer3;
//logic3
if (answer3 == 1)
    slytherin += 1;
  else if (answer3 == 2)
    hufflepuff += 1;
  else if (answer3 == 3)
    ravenclaw += 1;
  else if (answer3 == 4)
    gryffindor += 1;
  else
    std::cout << "Invalid input\n";

  //question4
  std::cout << "Q4) Which road tempts you most?\n1) The wide, sunny grassy lane\n2) The narrow, dark, lantern-lit alley\n3) The twisting, leaf-strewn path through woods\n4) The cobbled street lined (ancient buildings)\n";
  std::cin >> answer4;
//logic4
if (answer4 == 1)
    hufflepuff += 1;
  else if (answer4 == 2)
    slytherin += 1;
  else if (answer4 == 3)
    gryffindor += 1;
  else if (answer4 == 4)
    ravenclaw += 1;
  else
    std::cout << "Invalid input\n";

//house calculation
if (gryffindor > max)  
  max = gryffindor;
  house = "Gryffindor";
if (hufflepuff > max) 
  max = hufflepuff;
  house = "Hufflepuff";
if (ravenclaw > max) 
  max = ravenclaw;
  house = "Ravenclaw";
if (slytherin > max)
  max = slytherin;
  house = "Slytherin";
if(gryffindor and hufflepuff and ravenclaw and slytherin == 0)
    std::cout << "you know that you have to use only numbers to respond... right?";

//house declaration
if(gryffindor or hufflepuff or ravenclaw or slytherin != 0)
std::cout << house << "!\n";
Sleep(1000);
}
