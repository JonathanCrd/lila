# Lila

## By JonathanCrd & LizzieCC

Lila is a programming language design for exploring data andget usefull information and tips about the data declared in the program.

This was built with python and antlr4.

An example of all the special functions in this programming language is the following:
```
lila arreglos

var int[15] grades, age;
text[15] students;

main
{
    grades[0] = 90;
    grades[1] = 71;
    grades[2] = 95;
    grades[3] = 76;
    grades[4] = 9;
    grades[5] = 100;
    grades[6] = 90;
    grades[7] = 85;
    grades[8] = 99;
    grades[9] = 100;
    grades[10] = 100;
    grades[11] = 90;
    grades[12] = 97;
    grades[13] = 96;
    grades[14] = 89;

    age[0] = 18;
    age[1] = 18;
    age[2] = 19;
    age[3] = 19;
    age[4] = 17;
    age[5] = 18;
    age[6] = 19;
    age[7] = 16;
    age[8] = 18;
    age[9] = 19;
    age[10] = 19;
    age[11] = 20;
    age[12] = 20;
    age[13] = 20;
    age[14] = 21;

    students[0] = "LAURA";
    students[1] = "LUISA";
    students[2] = "JUAN";
    students[3] = "ANTONIO";
    students[4] = "LUIS";
    students[5] = "ITZEL";
    students[6] = "ERNESTO";
    students[7] = "ALEXANDER";
    students[8] = "FRANCISCO";
    students[9] = "JULIAN";
    students[10] = "BERTHA";
    students[11] = "MONICA";
    students[12] = "JULIAN";
    students[13] = "MANUEL";
    students[14] = "JESUS";

    // Where to start?
    tellMeWhatToUse(grades);

    // lets see the data visualy
    quickShow(grades,students);
    quickShow(grades,age);

    // Ok lets see the mean
    mean(grades);

    // Now lets see who are the atypical grades
    getOutliers(grades);

    // Lets see if there is a correlation between ages and grades
    pearsoneCorrelation(grades,age);

    // Lets bee cool and round the 99 to 100
    fillValue(grades,99,100);

    // Hmm... now lets think what would happend if those atypical students were not present in the data
    removeOutliers(grades);

    // lets see now
    printMeasures(grades);

}


```

To run your lila code file (.li), please run this:
```
python main.py <yourfile>.li
```

## Extra info:
To run antlr4: `g4 antlr4 -Dlanguage=Python3 Lila.g4`

On CodeExamples folder check exampleMaster
If you are using windows, run the next commands in cmd:
```
doskey antlr4=java org.antlr.v4.Tool $*
doskey grun =java org.antlr.v4.gui.TestRig $*
```