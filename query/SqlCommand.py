class QueryServices :

    createDB = (
        """
        CREATE DATABASE {DB_name};

        """
        )


    create_table = (
        """
        create table IF NOT EXISTS {Table} (
            {Columns},
            CONSTRAINT {Table}_pkey PRIMARY KEY ({PrimaryKey})
        );
        CREATE INDEX idx_{Table} ON {Table} USING btree ({ColumnIndex});
        CREATE OR REPLACE FUNCTION {ColumnTrigger}()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.{ColumnTrigger} = NOW();
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        CREATE TRIGGER {ColumnTrigger}
        BEFORE UPDATE ON {Table}
        FOR EACH ROW
        EXECUTE PROCEDURE {ColumnTrigger}();
        """
        )

    select = (
        """
        select 
            {Column}
        from {Table}
        where {FilterColumn};
        """
        )


    insert = (
        """
        insert into {Table} ({Column})
            values (
                {Value}
            );
        """
        )


    update = (
        """
        update {Table}
        set {SetColumn}
        where {FilterColumn}
        returning *;
        """
        )


    delete = (
        """
        delete from {Table}
        where {FilterColumn}
        """
        )
        
    truncate = (
        """TRUNCATE TABLE  {Table};"""
    )
        

    upsert = (
        """
        insert into {Table} ({Column})
        values (
            {Value}
        )
        on conflict ({PrimaryColumn})
        do update
           set {ColumnMarkUpdate}
        """
        )