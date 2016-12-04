using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    class Program
    {
        static void Main(string[] args)
        {
            
            string inputTest1 = "R2, L3";
            string inputTest2 = "R2, R2, R2";
            string inputTest3 = "R5, L5, R5, R3";

            Process(inputTest1);
            Process(inputTest2);
            Process(inputTest3);

            string input = "R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2, L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, L4, R3, L5, L3, R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, R2, L3, R3, L5, L1, R1, L2, L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, L4, L4, R3, R4, L4, R1, L3, L1, L1, R4, R1, L4, R1, L1, L3, R2, L2, R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3, R3, R1, R3, L4, R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5, R2, R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, L2, R4, R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1";
            Process(input);

            string inputTestTwice = "R8, R4, R4, R8";
            Process(inputTestTwice, true);

            Process(input, true);

            Console.ReadLine();
        }

        private static void Process(string input, bool twice = false)
        {
            Position finalPosition = Parse(input, twice);
            
            int distance = Math.Abs(finalPosition.x) + Math.Abs(finalPosition.y);

            Console.WriteLine("Position:       x = {0}, y = {1}", finalPosition.x, finalPosition.y);
            Console.WriteLine("Distance to HQ: " + distance);
            Console.WriteLine();
        }

        static Position Parse(string input, bool twice = false)
        {
            List<Position> positions = new List<Position>();

            Position position = new Position() { x = 0, y = 0 };
            positions.Add(position);

            var direction = 0;
            var steps = input.Split(',');
            foreach (var step in steps)
            {
                var current = step.Trim();
                var turn = current[0];

                direction = Turn(direction, turn);
                var length = int.Parse(current.Substring(1));

                switch (direction)
                {
                    case 0:
                        for (int i = 0; i < length; i++)
                        {
                            position = new Position() { x = position.x, y = position.y+1 };
                            if (twice && ContainsPos(positions, position)) return position;
                            positions.Add(position);
                        }
                        break;
                    case 1:
                        for (int i = 0; i < length; i++)
                        {
                            position = new Position() { x = position.x+1, y = position.y };
                            if (twice && ContainsPos(positions, position)) return position;
                            positions.Add(position);
                        }
                        break;
                    case 2:
                        for (int i = 0; i < length; i++)
                        {
                            position = new Position() { x = position.x, y = position.y-1 };
                            if (twice && ContainsPos(positions, position)) return position;
                            positions.Add(position);
                        }
                        break;
                    case 3:
                        for (int i = 0; i < length; i++)
                        {
                            position = new Position() { x = position.x-1, y = position.y };
                            if (twice && ContainsPos(positions, position)) return position;
                            positions.Add(position);
                        }
                        break;
                }                                
            }
            return position;
        }

        static int Turn(int direction, char turn)
        {
            if (turn == 'R') direction++;
            else if (turn == 'L') direction--;
            else throw new Exception("invalid turn");

            if (direction == -1) direction = 3;
            if (direction == 4) direction = 0;

            return direction;
        }

        static bool ContainsPos(List<Position> positions, Position position)
        {
            Debug.WriteLine("x = {0}, y = {1}", position.x, position.y);
            foreach (var p in positions)
            {
                if (p.x == position.x && p.y == position.y) return true;
            }
            return false;
        }

    }

    class Position
    {
        public int x;
        public int y;

        public Position()
        {
            x = 0;
            y = 0;
        }

        public Position(Position po)
        {
            x = po.x;
            y = po.y;
        }
    };

    

}
