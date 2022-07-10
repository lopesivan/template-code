// g++ -std=c++17 -c ex-01.cpp

template <typename T>
struct Fun_{
    using type = T;
};

template<>
struct Fun_<int>{
    using type = unsigned int;
};


template<>
struct Fun_<long>{
    using type = unsigned long;
};

Fun_<int>::type h = 3;

// Where  is  the  definition  of  the  function?  Programmers  who
// are  getting to  know  metafunctions  tend to ask such a
// question. In fact, lines 1–17 of the code snippet already define
// a function Fun_, and  line 19  uses Fun_<int>::type  to  return
// unsigned  int,  so  line  19  is  equivalent  to defining  an
// unsigned integer variable h and initialized with 3.
//

