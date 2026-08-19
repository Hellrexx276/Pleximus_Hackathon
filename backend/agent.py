import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

from backend.tools.calculator import calculator
from backend.tools.weather import get_weather
from backend.tools.currency import convert_currency
from backend.tools.measurement import convert_measurement
from backend.tools.text_utility import text_utility


# =========================================================
# ENVIRONMENT
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(
    ENV_FILE,
    override=True
)


# =========================================================
# GEMINI CLIENT
# =========================================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        f"GEMINI_API_KEY was not found. "
        f"Checked: {ENV_FILE}"
    )

client = genai.Client(
    api_key=api_key
)


# =========================================================
# TOOL DEFINITIONS
# =========================================================

tools = [
    types.Tool(
        function_declarations=[

            # =================================================
            # CALCULATOR
            # =================================================

            types.FunctionDeclaration(
                name="calculator",

                description=(
                    "Perform mathematical calculations. "
                    "Use this tool whenever the user asks "
                    "you to calculate a mathematical expression."
                ),

                parameters=types.Schema(
                    type="OBJECT",

                    properties={
                        "expression": types.Schema(
                            type="STRING",

                            description=(
                                "Mathematical expression to calculate. "
                                "Example: 25 * 100 / 4"
                            ),
                        )
                    },

                    required=[
                        "expression"
                    ],
                ),
            ),

            # =================================================
            # WEATHER
            # =================================================

            types.FunctionDeclaration(
                name="get_weather",

                description=(
                    "Get the current weather for a city. "
                    "Use this when the user asks about "
                    "current weather, temperature, humidity, "
                    "or weather conditions."
                ),

                parameters=types.Schema(
                    type="OBJECT",

                    properties={
                        "city": types.Schema(
                            type="STRING",

                            description=(
                                "Name of the city. "
                                "Example: Mumbai."
                            ),
                        )
                    },

                    required=[
                        "city"
                    ],
                ),
            ),

            # =================================================
            # CURRENCY CONVERTER
            # =================================================

            types.FunctionDeclaration(
                name="convert_currency",

                description=(
                    "Convert an amount of money from one "
                    "currency to another currency."
                ),

                parameters=types.Schema(
                    type="OBJECT",

                    properties={

                        "amount": types.Schema(
                            type="NUMBER",

                            description=(
                                "Amount of money to convert."
                            ),
                        ),

                        "from_currency": types.Schema(
                            type="STRING",

                            description=(
                                "Currency code to convert from. "
                                "Examples: USD, EUR, INR."
                            ),
                        ),

                        "to_currency": types.Schema(
                            type="STRING",

                            description=(
                                "Currency code to convert to. "
                                "Examples: USD, EUR, INR."
                            ),
                        ),
                    },

                    required=[
                        "amount",
                        "from_currency",
                        "to_currency",
                    ],
                ),
            ),

            # =================================================
            # MEASUREMENT CONVERTER
            # =================================================

            types.FunctionDeclaration(
                name="convert_measurement",

                description=(
                    "Convert a measurement from one unit "
                    "to another. Supports units such as "
                    "meters, feet, kilometers, miles, "
                    "inches, centimeters, kilograms, pounds, "
                    "Celsius, and Fahrenheit."
                ),

                parameters=types.Schema(
                    type="OBJECT",

                    properties={

                        "value": types.Schema(
                            type="NUMBER",

                            description=(
                                "The numerical value to convert."
                            ),
                        ),

                        "from_unit": types.Schema(
                            type="STRING",

                            description=(
                                "Unit to convert from. "
                                "Examples: feet, meters, kg, "
                                "miles, Celsius."
                            ),
                        ),

                        "to_unit": types.Schema(
                            type="STRING",

                            description=(
                                "Unit to convert to. "
                                "Examples: meters, feet, kg, "
                                "miles, Fahrenheit."
                            ),
                        ),
                    },

                    required=[
                        "value",
                        "from_unit",
                        "to_unit",
                    ],
                ),
            ),

            # =================================================
            # TEXT / WORD UTILITY
            # =================================================

            types.FunctionDeclaration(
                name="text_utility",

                description=(
                    "Perform local text and string operations. "
                    "Use this tool for tasks such as counting "
                    "words, counting characters, converting text "
                    "to uppercase or lowercase, reversing text, "
                    "removing extra spaces, counting occurrences "
                    "of a word, or checking whether text is a "
                    "palindrome."
                ),

                parameters=types.Schema(
                    type="OBJECT",

                    properties={

                        "text": types.Schema(
                            type="STRING",

                            description=(
                                "The text on which the operation "
                                "should be performed."
                            ),
                        ),

                        "operation": types.Schema(
                            type="STRING",

                            description=(
                                "The operation to perform. "
                                "Possible values: word_count, "
                                "character_count, "
                                "character_count_no_spaces, "
                                "uppercase, lowercase, reverse, "
                                "remove_extra_spaces, count_word, "
                                "palindrome."
                            ),
                        ),

                        "search_word": types.Schema(
                            type="STRING",

                            description=(
                                "The specific word to search for "
                                "when using the count_word operation."
                            ),
                        ),
                    },

                    required=[
                        "text",
                        "operation",
                    ],
                ),
            ),
        ]
    )
]


# =========================================================
# TOOL EXECUTOR
# =========================================================

def execute_tool(
    name: str,
    args: dict
):

    if name == "calculator":

        return calculator(
            **args
        )

    elif name == "get_weather":

        return get_weather(
            **args
        )

    elif name == "convert_currency":

        return convert_currency(
            **args
        )

    elif name == "convert_measurement":

        return convert_measurement(
            **args
        )

    elif name == "text_utility":

        return text_utility(
            **args
        )

    return {
        "error": f"Unknown tool: {name}"
    }


# =========================================================
# AI AGENT
# =========================================================

def chat_with_agent(
    user_message: str
):

    # =====================================================
    # STEP 1
    #
    # Send the user's request to Gemini.
    #
    # Gemini decides whether a tool is needed and,
    # if needed, which tool should be used.
    # =====================================================

    response = client.models.generate_content(

        model="gemini-3.6-flash",

        contents=user_message,

        config=types.GenerateContentConfig(
            tools=tools
        ),
    )


    # =====================================================
    # STEP 2
    #
    # Check whether Gemini requested a tool/function call.
    # =====================================================

    function_calls = []

    for part in response.candidates[0].content.parts:

        if part.function_call:

            function_calls.append(
                part.function_call
            )


    # =====================================================
    # STEP 3
    #
    # No tool required.
    #
    # Example:
    # "Hello, how are you?"
    #
    # Gemini responds normally.
    # =====================================================

    if not function_calls:

        return response.text


    # =====================================================
    # STEP 4
    #
    # Execute the tool(s) selected by Gemini.
    # =====================================================

    tool_results = []

    for function_call in function_calls:

        name = function_call.name

        args = dict(
            function_call.args
        )

        print("\n==============================")
        print(
            "AI SELECTED TOOL:",
            name
        )
        print(
            "TOOL ARGUMENTS:",
            args
        )
        print("==============================")


        # Execute the selected Python tool
        result = execute_tool(
            name,
            args
        )


        print(
            "TOOL RESULT:",
            result
        )


        # =================================================
        # Send the tool result back to Gemini.
        # =================================================

        tool_results.append(

            types.Part.from_function_response(

                name=name,

                response=result,
            )
        )


    # =====================================================
    # STEP 5
    #
    # Gemini receives the tool result and generates
    # the final natural-language response.
    # =====================================================

    final_response = client.models.generate_content(

        model="gemini-3.6-flash",

        contents=[
            user_message,

            response.candidates[0].content,

            *tool_results,
        ],

        config=types.GenerateContentConfig(
            tools=tools
        ),
    )


    return final_response.text