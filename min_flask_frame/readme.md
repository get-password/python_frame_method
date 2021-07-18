

##启动
* export ops_config=local|production && python manage.py runserver

##flask-sqlacodegen

        flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask
        flask-sqlacodegen “mysql://root:123456@127.0.0.1/tf_train_data” --tables train_info --outfile "F:/mooc/flask_owner_use_min/common/models/tf_train/train_info.py"  --flask


##sql索引
            方法一（用于层层筛选数据）   query = Food.query
                    rule = or_(Food.name.ilike("%{0}%".format(req['mix_kw'])), Food.tags.ilike("%{0}%".format(req['mix_kw'])))
                    query = query.filter( rule )
                    list = query.order_by( Food.id.desc() ).offset( offset ).limit( app.config['PAGE_SIZE'] ).all()                    

            方法二   info = Food.query.filter_by( id =id ).first()

            方法三   Food.query.filter( Food.status == int( req['status'] ) )

    model_food = Food()
    db.session.add(model_food)
    db.session.commit()