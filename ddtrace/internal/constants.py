PROPAGATION_STYLE_DATADOG = "datadog"
PROPAGATION_STYLE_B3 = "b3multi"
PROPAGATION_STYLE_B3_SINGLE_HEADER = "b3 single header"
_PROPAGATION_STYLE_W3C_TRACECONTEXT = "tracecontext"
_PROPAGATION_STYLE_NONE = "none"
_PROPAGATION_STYLE_DEFAULT = "tracecontext,datadog"
PROPAGATION_STYLE_ALL = (
    _PROPAGATION_STYLE_W3C_TRACECONTEXT,
    PROPAGATION_STYLE_DATADOG,
    PROPAGATION_STYLE_B3,
    PROPAGATION_STYLE_B3_SINGLE_HEADER,
    _PROPAGATION_STYLE_NONE,
)
W3C_TRACESTATE_KEY = "tracestate"
W3C_TRACEPARENT_KEY = "traceparent"
W3C_TRACESTATE_ORIGIN_KEY = "o"
W3C_TRACESTATE_SAMPLING_PRIORITY_KEY = "s"
DEFAULT_SAMPLING_RATE_LIMIT = 100
SAMPLING_DECISION_TRACE_TAG_KEY = "_dd.p.dm"
DEFAULT_SERVICE_NAME = "unnamed_python_service"
# Used to set the name of an integration on a span
COMPONENT = "component"
HIGHER_ORDER_TRACE_ID_BITS = "_dd.p.tid"
MAX_UINT_64BITS = (1 << 64) - 1
SPAN_API_DATADOG = "datadog"
SPAN_API_OTEL = "otel"
SPAN_API_OPENTRACING = "opentracing"
BLOCKED_RESPONSE_HTML = """
<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta name="viewport"
content="width=device-width,initial-scale=1"> <title>You've been blocked</title>
<style>a, body, div, html, span{margin: 0; padding: 0; border: 0; font-size: 100%;
font: inherit; vertical-align: baseline}body{background: -webkit-radial-gradient(26% 19%,
circle, #fff, #f4f7f9); background: radial-gradient(circle at 26% 19%, #fff, #f4f7f9); display:
-webkit-box; display: -ms-flexbox; display: flex; -webkit-box-pack: center; -ms-flex-pack: center;
justify-content: center; -webkit-box-align: center; -ms-flex-align: center; align-items: center;
-ms-flex-line-pack: center; align-content: center; width: 100%; min-height: 100vh; line-height: 1;
flex-direction: column}p{display: block}main{text-align: center; flex: 1; display: -webkit-box;
display: -ms-flexbox; display: flex; -webkit-box-pack: center; -ms-flex-pack: center;
justify-content: center; -webkit-box-align: center; -ms-flex-align: center; align-items: center;
-ms-flex-line-pack: center; align-content: center; flex-direction: column}p{font-size: 18px;
line-height: normal; color: #646464; font-family: sans-serif; font-weight: 400}a{color:
#4842b7}footer{width: 100%; text-align: center}footer p{font-size: 16px}</style></head><body>
<main> <p>Sorry, you cannot access this page. Please contact the customer service team.</p></main>
<footer> <p>Security provided by
<a href="https://www.datadoghq.com/product/security-platform/application-security-monitoring/"
target="_blank">Datadog</a></p></footer></body></html>"""
BLOCKED_RESPONSE_JSON = (
    '{"errors": [{"title": "You\'ve been blocked", "detail": "Sorry, you cannot access '
    'this page. Please contact the customer service team. Security provided by Datadog."}]}'
)
HTTP_REQUEST_BLOCKED = "http.request.blocked"
RESPONSE_HEADERS = "http.response.headers"
HTTP_REQUEST_QUERY = "http.request.query"
HTTP_REQUEST_COOKIE_VALUE = "http.request.cookie.value"
HTTP_REQUEST_COOKIE_NAME = "http.request.cookie.name"
HTTP_REQUEST_PATH = "http.request.path"
HTTP_REQUEST_HEADER_NAME = "http.request.header.name"
HTTP_REQUEST_HEADER = "http.request.header"
HTTP_REQUEST_PARAMETER = "http.request.parameter"
HTTP_REQUEST_BODY = "http.request.body"
HTTP_REQUEST_PATH_PARAMETER = "http.request.path.parameter"
REQUEST_PATH_PARAMS = "http.request.path_params"

MESSAGING_SYSTEM = "messaging.system"

FLASK_ENDPOINT = "flask.endpoint"
FLASK_VIEW_ARGS = "flask.view_args"
FLASK_URL_RULE = "flask.url_rule"

_HTTPLIB_NO_TRACE_REQUEST = "_dd_no_trace"
