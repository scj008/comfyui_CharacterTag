import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "Opentag Monitor",
    async setup() {
        console.log("✅ 插件已加载 - 等待工作流准备就绪");

        // 存储已注册监听器的节点ID
        const registeredNodes = new Set();

        // 节点检查与同步设置函数
        const setupNodeSync = () => {
            if (!app.graph?.nodes) return;

            // 查找所有Opentag节点
            const opentagNodes = app.graph.nodes.filter(node =>
                node?.type.includes("打开提示词标签") ||
                node?.type === "打开提示词标签"
            );

            // 为符合条件的节点设置同步
            opentagNodes.forEach(node => {
                const inputTextWidget = node.widgets?.find(w => w.name === "input_text");
                const inputText1Widget = node.widgets?.find(w => w.name === "input_text1");

                // 检查是否已注册
                if (inputTextWidget && inputText1Widget && !registeredNodes.has(node.id)) {
                    console.log("🔔 为节点 " + node.id + " 注册值同步监听器");

                    // 初始值同步
                    inputText1Widget.value = inputTextWidget.value;
                    if (inputText1Widget.onChange) inputText1Widget.onChange();

                    // 保存原始回调
                    const originalCallback = inputTextWidget.callback;

                    // 设置带防抖的新回调
                    let debounceTimer;
                    inputTextWidget.callback = (value, widget, node) => {
                        // console.log("🔄 input_text 值变更: " + value);

                        // 执行原始回调
                        if (originalCallback) originalCallback(value, widget, node);

                        // 清除之前的定时器
                        clearTimeout(debounceTimer);

                        // 设置新的防抖定时器
                        debounceTimer = setTimeout(() => {
                            //console.log("🔄 input_text1 值同步: " + value);
                            // 值同步
                            inputText1Widget.value = value;

                            // 刷新显示
                            if (inputText1Widget.onChange) inputText1Widget.onChange();

                            // 刷新画布
                            try {
                                app.canvas?.setDirty(true);
                            } catch (e) {
                                console.warn("刷新画布失败:", e);
                            }
                        }, 300); // 300ms防抖
                    };

                    // 标记为已注册
                    registeredNodes.add(node.id);
                }
            });
        };

        // 初始节点设置
        setTimeout(setupNodeSync, 500);

        // 节点添加事件处理
        app.graph.onNodeAdded = function(node) {
            setupNodeSync();
        };

        // 节点移除事件处理
        app.graph.onNodeRemoved = function(node) {
            registeredNodes.delete(node.id);
        };
    },
});
