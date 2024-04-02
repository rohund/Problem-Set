{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e07cbab2-2e55-4ccb-9c24-948abada59ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Exercise 0 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d520f931-ef54-4d72-bff1-23c3e6a45865",
   "metadata": {},
   "outputs": [],
   "source": [
    "def github() -> str:\n",
    "    \"\"\"\n",
    "    Some docstrings.\n",
    "    \"\"\"\n",
    "\n",
    "    return \"https://github.com/<rohund>/<Problem-Set-1>/blob/main/<filename.py>\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0f2879d-2b63-4550-8192-1451d737274c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Exercise 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a9c6db02-47dc-42b5-a752-c25d056dc2b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'evens': 2, 'odds': 4}\n"
     ]
    }
   ],
   "source": [
    "def evens_and_odds(n: int) -> dict:\n",
    "    \"\"\"\n",
    "    Returns a dictionary with the sum of even and odd numbers less than n.\n",
    "    \n",
    "    Args:\n",
    "    n (int): A natural number.\n",
    "    \n",
    "    Returns:\n",
    "    dict: A dictionary with keys 'evens' and 'odds' representing the sum of even and odd numbers less than n respectively.\n",
    "    \"\"\"\n",
    "    evens_sum = sum(i for i in range(n) if i % 2 == 0)\n",
    "    odds_sum = sum(i for i in range(n) if i % 2 != 0)\n",
    "    return {'evens': evens_sum, 'odds': odds_sum}\n",
    "\n",
    "# Test\n",
    "print(evens_and_odds(4))  # Output: {'evens': 2, 'odds': 4}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "31f8aa21-3965-4561-b558-7a4fad0b8f55",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Exercise 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4c0b2b32-c7b4-4786-a39a-85d4487387eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "There are 2 days between the two dates\n"
     ]
    }
   ],
   "source": [
    "from typing import Union\n",
    "from datetime import datetime\n",
    "\n",
    "def time_diff(date_1: str, date_2: str, out: str = 'float') -> Union[str, float]:\n",
    "    \"\"\"\n",
    "    Calculates the time difference between two dates.\n",
    "    \n",
    "    Args:\n",
    "    date_1 (str): The first date in the format 'YYYY-MM-DD'.\n",
    "    date_2 (str): The second date in the format 'YYYY-MM-DD'.\n",
    "    out (str): Specifies the output format. Can be 'float' or 'string'. Default is 'float'.\n",
    "    \n",
    "    Returns:\n",
    "    Union[str, float]: Depending on the 'out' parameter, returns either a float representing the time difference in days,\n",
    "    or a string indicating the time difference.\n",
    "    \"\"\"\n",
    "    # Convert date strings to datetime objects\n",
    "    date_1 = datetime.strptime(date_1, '%Y-%m-%d')\n",
    "    date_2 = datetime.strptime(date_2, '%Y-%m-%d')\n",
    "    \n",
    "    # Calculate the absolute time difference in days\n",
    "    time_difference = abs((date_1 - date_2).days)\n",
    "    \n",
    "    # Output based on the 'out' parameter\n",
    "    if out == 'string':\n",
    "        return f\"There are {time_difference} days between the two dates\"\n",
    "    else:\n",
    "        return time_difference\n",
    "\n",
    "# Test\n",
    "print(time_diff('2020-01-01', '2020-01-02', 'float'))  # Output: 1\n",
    "print(time_diff('2020-01-03', '2020-01-01', 'string'))  # Output: \"There are 2 days between the two dates\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c90d688-b84d-4534-9b0f-86cfdaa93c6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Exercise 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cae567ea-916c-4e15-8072-12b4357e1dd0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['c', 'b', 'a']\n"
     ]
    }
   ],
   "source": [
    "def reverse(in_list: list) -> list:\n",
    "    \"\"\"\n",
    "    Returns the list in reverse order.\n",
    "    \n",
    "    Args:\n",
    "    in_list (list): Input list.\n",
    "    \n",
    "    Returns:\n",
    "    list: The input list in reverse order.\n",
    "    \"\"\"\n",
    "    reversed_list = []\n",
    "    # Traverse the input list in reverse order and append elements to the reversed list\n",
    "    for i in range(len(in_list) - 1, -1, -1):\n",
    "        reversed_list.append(in_list[i])\n",
    "    return reversed_list\n",
    "\n",
    "# Test\n",
    "print(reverse(['a', 'b', 'c']))  # Output: ['c', 'b', 'a']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8e61637-9d67-4b3d-b36b-17062df94b8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Exercise 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d8521652-fd1b-4982-a983-74b2e29f8874",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.5\n"
     ]
    }
   ],
   "source": [
    "def prob_k_heads(n: int, k: int) -> float:\n",
    "    \"\"\"\n",
    "    Calculate the probability of getting exactly k heads in n coin flips.\n",
    "\n",
    "    Args:\n",
    "    n (int): Number of coin flips.\n",
    "    k (int): Number of heads.\n",
    "\n",
    "    Returns:\n",
    "    float: Probability of getting exactly k heads.\n",
    "    \"\"\"\n",
    "    # Probability of getting a single head\n",
    "    p_head = 0.5\n",
    "    \n",
    "    # Calculate the binomial coefficient (n choose k)\n",
    "    def binomial_coefficient(n, k):\n",
    "        if k == 0 or k == n:\n",
    "            return 1\n",
    "        else:\n",
    "            return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)\n",
    "    \n",
    "    # Calculate the probability using the binomial probability formula\n",
    "    probability = binomial_coefficient(n, k) * (p_head ** k) * ((1 - p_head) ** (n - k))\n",
    "    \n",
    "    return probability\n",
    "\n",
    "# Test the function\n",
    "print(prob_k_heads(1, 1))  # Output: 0.5\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
