# Cookuecutter collection
> A cookie cutter collection

![](https://cdn.thisiswhyimbroke.com/buying-guides-thumb/833/killer-chicken-funny-cookie-cutter_400x.jpg)

## Usage

```
cookiecutter https://github.com/roymanigley/cookiecutter-collection
```
### Select the template you want
```
Select a template
    1 - Dockerfile (A cookiecutter template for a Dockerfile)
    2 - docker-compose (A cookiecutter template for a docker-compose.yaml)
    3 - Python Package (A Python Package template)
    4 - VIM setup (A VIM setup template)
    5 - Penetration Testing (A Penetration Testing tool suite)
    6 - Jinja (A Jinja template)
    7 - Django Rest Framework (A Django Rest Framework template with OAuth2)
    8 - Django Ninja (A Django Ninja template with OAuth2)
    9 - Django Template (A Django Template using Daisy UI template with Session Authentication)
    10 - HTML (A HTML template using matrializecss)
    11 - Cookiecutter (A Cookiecutter template)
    Choose from [1/2/3/4/5/6/7/8/9/10/11] (1):
```

### After generation
> when you used one of the templates:  
>  - `Django Rest Framework`
>  - `Django Ninja` 
>  - `Django Template`  
>   
> Then you can define your models using:  
> `./management.py cookiecutter`  
>   
> After you have defined your models you have to commit the changes (the `cookiecutter.json` will be adapted)  
>   
> Then you can run `./management.py cookiecutter_run` to regenerate your project