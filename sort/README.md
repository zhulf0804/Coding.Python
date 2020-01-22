## 常用排序算法的python实现
+ O(n^2) [排序算法测试OJ](https://www.lintcode.com/problem/sort-integers/description)
+ O(n*logn) [排序算法测试OJ](https://www.lintcode.com/problem/sort-integers-ii/description)


| 算法 | 类别 | 时间复杂度 | 时间复杂度(最好) | 时间复杂度(最坏) | 空间复杂度 | 稳定性 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 冒泡排序 | 比较，交换 | O(n^2) | | | O(1) | 稳定 |
| 选择排序 | 比较，选择 | O(n^2) | | | O(1) | **不稳定** |
| 插入排序 | 比较，插入 | O(n^2) | O(n) | O(n^2) | O(1) | 稳定 |
| 希尔排序 | 比较, 插入 | O(nlogn) | O(nlogn) | O(n) | O(1) | 不稳定 |
| 快速排序 | 比较, 交换 | O(nlogn) | O(nlogn) | O(n^2) | O(logn) | 不稳定 |
| 归并排序 | 比较, 归并 | O(nlogn) | O(nlogn) | O(nlogn) | | 稳定 |
| 堆排序 | 比较, 选择 | O(nlogn) | O(nlogn) | O(nlogn) | O(1) | 不稳定 |
| 基数排序 | 非比较
| 计数排序 | 非比较
| 桶排序 | 非比较 

## 参考资料
- [https://www.cnblogs.com/onepixel/p/7674659.html](https://www.cnblogs.com/onepixel/p/7674659.html)
 