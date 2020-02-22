# Fx Qwerty

Various keyboard layouts for your F(x)tec Pro1 physical keyboard:

- F(x)tec Pro1 Qwerty - US
- F(x)tec Pro1 Qwerty - US - Fn+Tab
- F(x)tec Pro1 Qwerty - US - Shift as Fn
- F(x)tec Pro1 Qwerty - US - Shift as Fn - Fn+Tab

See the [Fx Qwerty website](https://slions.net/resources/fx-qwerty.7/) for detailed layout maps.
The layouts are provided via the Android standard layouts mechanism and are selectable in Android settings - no root required.

## Installing

Download from [Fx Qwerty website](https://slions.net/resources/fx-qwerty.7/).

## Building

Python 3 is required to build Fx Qwerty.

The project uses Gradle and can be built with Android Studio or via commandline, for example:

```
export JAVA_HOME="$HOME/android-studio/jre"
export ANDROID_HOME="$HOME/Android/Sdk"
./gradlew assembleDebug
```

## Layout files

Most layouts are generated from other layouts automatically by `generate_layouts.py`
during the build process and are therefore not found in this repository.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Credits

Fx Qwerty was forked from [FinQwerty](https://github.com/anssih/finqwerty).

