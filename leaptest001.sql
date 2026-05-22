-- =============================================
-- copydata 脚本：用于 Git 测试前准备测试数据
-- 功能：创建测试表 + 插入测试数据
-- =============================================

-- 1. 如果表存在，先删除
DROP TABLE IF EXISTS test_data_table;

-- 2. 创建测试表
CREATE TABLE test_data_table (
    id INT,
    name STRING,
    age INT
);

-- 3. 插入测试数据（复制数据 → 这就是 copydata 的含义）
INSERT INTO test_data_table VALUES
(1, 'test_user_01', 20),
(2, 'test_user_02', 25),
(3, 'test_user_03', 30);

-- 4. 查看数据是否生成成功
SELECT * FROM test_data_table;
EOF
