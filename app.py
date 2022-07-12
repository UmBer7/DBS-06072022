{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,render_template,request\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        model = joblib.load(\"regression.jl\")\n",
    "        r = model.predict([[rates]])\n",
    "        return (render_template(\"index.html\",result = r))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result = \"WAITING\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "[2022-07-09 10:52:23,876] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"C:\\Users\\LZC\\AppData\\Local\\Temp\\ipykernel_15420\\2266996312.py\", line 9, in index\n",
      "    return(render_template(\"D:/html_code/index.html\",result = \"WAITING\"))\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\jinja2\\environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\jinja2\\environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\jinja2\\environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\jinja2\\loaders.py\", line 115, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: D:/html_code/index.html\n",
      "127.0.0.1 - - [09/Jul/2022 10:52:23] \"GET / HTTP/1.1\" 500 -\n",
      "[2022-07-09 10:52:27,632] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"C:\\Users\\LZC\\AppData\\Local\\Temp\\ipykernel_15420\\2266996312.py\", line 9, in index\n",
      "    return(render_template(\"D:/html_code/index.html\",result = \"WAITING\"))\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\jinja2\\environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\jinja2\\environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\jinja2\\environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\jinja2\\loaders.py\", line 115, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"d:\\anaconda\\lib\\site-packages\\flask\\templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: D:/html_code/index.html\n",
      "127.0.0.1 - - [09/Jul/2022 10:52:27] \"GET / HTTP/1.1\" 500 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.12 ('base')",
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
   "version": "3.9.12"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "5179d32cf6ec497baf3f8a3ef987cc77c5d2dc691fdde20a56316522f61a7323"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
