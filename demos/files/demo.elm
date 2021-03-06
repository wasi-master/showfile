import Browser
import Html exposing (div, button, text)
import Html.Events exposing (onClick)

type Msg
    = Increment

main =
    Browser.sandbox
        { init = 0
        , update = \msg model -> model + 1
        , view = view
        }

view model =
    div []
        [ div [] [ text (String.fromInt model) ]
        , button [ onClick Increment ] [ text "+" ]
        ]

chars =
    String.cons 'C' <| String.cons 'h' <| "ars"